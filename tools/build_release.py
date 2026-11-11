#!/usr/bin/env python3
"""Build a release of the public MHA: Your Story update repository.

Input: the published Creator API world document (as returned by GET /worlds/<id>), in either the
old layout (triggers, quests ... at the top of initialGameState) or the Voyage 2.52 layout
(triggerDefinitions, parties[""]). The release is always written in the 2.52 layout, the one live
worlds and saves use.

Writes (all paths relative to the repository root):
  world/MHA_Your_Story.json          the full world document (data.world)
  world/MHA_Your_Story.studio.json   initialGameState only (the editor's world JSON)
  sections/<section>.json            one file per section, the exact value of that section
  entries/<section>/<entry>.json     one file per entry for the big sections (triggers, NPCs, ...)
  entries/<section>/INDEX.md         entry name -> file
  releases/<label>.hashes.json       SHA-256 of every section and entry in this release
  releases/<label>.changes.md        the machine change list against the previous release
  SECTIONS.md                        every section: category, size, entries, changed this release
  MANIFEST.json                      release metadata and file hashes

Usage:
  python tools/build_release.py --label 11.02 --source <world.json> [--previous releases/<old>.hashes.json]

After a run, write the human "why" for the release in CHANGES.md (the machine list is in
releases/<label>.changes.md) and commit everything in one commit.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, "world", "MHA_Your_Story.json")
STUDIO = os.path.join(ROOT, "world", "MHA_Your_Story.studio.json")
SECTIONS_DIR = os.path.join(ROOT, "sections")
ENTRIES_DIR = os.path.join(ROOT, "entries")
RELEASES_DIR = os.path.join(ROOT, "releases")

PARTY_KEYS = ("quests", "questTriggers", "arcs", "narrativeEvents")
KNOWN_SECS = ("npcs", "locations", "factions", "regions", "realms")

# category, description. content = authored world content, settings = rules the engine reads (both
# safe to copy into a save); meta = platform bookkeeping (leave alone).
SECTIONS = {
    "abilities": ("content", "Every Quirk technique and ability, with unlock levels and effects"),
    "aiInstructions": ("settings", "Narrator and engine instruction blocks (story, NPCs, encounters, starts)"),
    "attributeSettings": ("settings", "Attributes and their modifiers"),
    "authorSeeds": ("content", "Writing-style seeds for the narrator"),
    "characterArchetypes": ("content", "Templates for generated characters"),
    "characterCreationMusic": ("settings", "Music used during character creation"),
    "characterCreationSettings": ("settings", "Character creator steps and options"),
    "combatSettings": ("settings", "Damage types and combat rules"),
    "compatibilityRevision": ("meta", "Voyage layout revision"),
    "death": ("settings", "What happens when a character goes down"),
    "encounterElements": ("content", "Building blocks for generated encounters"),
    "endGame": ("settings", "Ending narration"),
    "factions": ("content", "Hero agencies, the League, U.A. and other groups"),
    "gameModes": ("content", "Play modes and their narrator rules"),
    "gameplayMusicSettings": ("settings", "Gameplay music"),
    "heroesVersion": ("meta", "World schema version"),
    "imagePromptConfiguration": ("settings", "Image prompt routing for portraits and scenes"),
    "itemSettings": ("settings", "Item categories, tiers and slots"),
    "itemTypes": ("content", "Every item: gear, costumes, food, documents, currency"),
    "locationArchetypes": ("content", "Templates for generated locations"),
    "locationSettings": ("settings", "Location rules"),
    "locations": ("content", "Every place, its areas, pictures and hidden info"),
    "mods": ("meta", "Installed mods"),
    "nameFilterSettings": ("settings", "Name filter rules"),
    "narratorStyle": ("settings", "Narrator voice"),
    "npcTypes": ("content", "Types used for generated NPCs"),
    "npcs": ("content", "Every character: profiles, stages, looks and hidden info"),
    "otherSettings": ("settings", "Miscellaneous numbers"),
    "parties.arcs": ("content", "Long story arcs (inside Parties)"),
    "parties.narrativeEvents": ("content", "Canon events and side events (inside Parties)"),
    "parties.questTriggers": ("content", "Quest progress triggers (inside Parties)"),
    "parties.quests": ("content", "Every quest (inside Parties)"),
    "premadeCharacters": ("content", "The premade player characters"),
    "progressionSettings": ("settings", "Levelling cadence"),
    "randomNames": ("content", "Random name pools"),
    "realms": ("content", "The realm (Japan)"),
    "regionArchetypes": ("content", "Templates for generated regions"),
    "regions": ("content", "Map regions"),
    "relationshipStages": ("settings", "Relationship stages"),
    "resourceSettings": ("settings", "Health, Stamina and Strain"),
    "skillSettings": ("settings", "Skill rules"),
    "skills": ("content", "Every skill"),
    "storySettings": ("settings", "Story settings"),
    "storyStarts": ("content", "Every story start"),
    "successLevelSettings": ("settings", "Success level narration"),
    "tipSettings": ("settings", "Loading tips"),
    "traitCategories": ("content", "Trait categories (Paths, Quirk families, backgrounds ...)"),
    "traits": ("content", "Every trait: Paths, Quirks, backgrounds and their narrator rules"),
    "triggerDefinitions": ("content", "Every trigger: the clock, skips, events, wardrobe, travel ..."),
    "worldLore": ("content", "World lore entries"),
    "worldVoices": ("settings", "Voice assignments"),
}
# sections whose value is a map of named entries: each entry also gets its own file
ENTRY_SECTIONS = ("abilities", "aiInstructions", "characterArchetypes", "encounterElements", "factions", "gameModes",
                  "itemTypes", "locationArchetypes", "locations", "npcTypes", "npcs", "parties.narrativeEvents",
                  "parties.questTriggers", "parties.quests", "regionArchetypes", "regions", "skills", "storyStarts",
                  "traitCategories", "traits", "triggerDefinitions", "worldLore", "worldVoices")


def to_new(G):
    """Old layout -> Voyage 2.52 layout (the live one)."""
    G = json.loads(json.dumps(G))
    if "triggers" in G:
        G["triggerDefinitions"] = G.pop("triggers")
    if "parties" not in G:
        G["parties"] = {"": {k: G.pop(k) for k in PARTY_KEYS if k in G}}
    for sec in KNOWN_SECS:
        for v in (G.get(sec) or {}).values():
            if isinstance(v, dict) and "known" in v:
                v["initialKnown"] = v.pop("known")
    return G


def sections_of(G):
    out = {}
    for k, v in G.items():
        if k == "parties":
            for pk, pv in (v.get("") or {}).items():
                out["parties." + pk] = pv
        else:
            out[k] = v
    return out


def dump(v):
    return json.dumps(v, ensure_ascii=False, indent=2, sort_keys=False) + "\n"


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def safe_name(key, used):
    n = re.sub(r'[\\/:*?"<>|\x00-\x1f]', "_", key).strip().rstrip(".") or "_"
    n = n[:120]
    base, i = n, 2
    while n.lower() in used:
        n = f"{base}~{i}"
        i += 1
    used.add(n.lower())
    return n


def label_of(key, v):
    if isinstance(v, dict):
        for f in ("name", "title", "displayName"):
            if isinstance(v.get(f), str) and v[f].strip():
                return v[f].strip()
    return key


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", required=True)
    ap.add_argument("--source", required=True)
    ap.add_argument("--previous")
    ap.add_argument("--published", default="")
    a = ap.parse_args()

    doc = json.load(open(a.source, encoding="utf-8"))
    world = doc["data"]["world"] if "data" in doc else doc
    world = json.loads(json.dumps(world))
    world["initialGameState"] = to_new(world["initialGameState"])
    G = world["initialGameState"]
    S = sections_of(G)
    unknown = sorted(set(S) - set(SECTIONS))
    if unknown:
        sys.exit("ERROR: sections without a category in SECTIONS: " + ", ".join(unknown))

    for d in (SECTIONS_DIR, ENTRIES_DIR):
        if os.path.isdir(d):
            shutil.rmtree(d)
        os.makedirs(d)
    os.makedirs(os.path.dirname(FULL), exist_ok=True)
    os.makedirs(RELEASES_DIR, exist_ok=True)

    open(FULL, "w", encoding="utf-8", newline="\n").write(dump({"data": {"world": world}}))
    open(STUDIO, "w", encoding="utf-8", newline="\n").write(dump(G))

    hashes = {"label": a.label, "sections": {}, "entries": {}}
    rows = []
    for name in sorted(S):
        v = S[name]
        txt = dump(v)
        open(os.path.join(SECTIONS_DIR, name + ".json"), "w", encoding="utf-8", newline="\n").write(txt)
        hashes["sections"][name] = sha(json.dumps(v, ensure_ascii=False, sort_keys=True))
        n_entries = ""
        if name in ENTRY_SECTIONS and isinstance(v, dict):
            d = os.path.join(ENTRIES_DIR, name)
            os.makedirs(d)
            used, idx, eh = set(), [], {}
            for key in v:
                fn = safe_name(key, used)
                open(os.path.join(d, fn + ".json"), "w", encoding="utf-8", newline="\n").write(dump({key: v[key]}))
                eh[key] = {"file": fn + ".json", "name": label_of(key, v[key]),
                           "sha": sha(json.dumps(v[key], ensure_ascii=False, sort_keys=True))}
                idx.append((label_of(key, v[key]), key, fn))
            hashes["entries"][name] = eh
            n_entries = len(v)
            lines = [f"# {name}: {len(v)} entries ({a.label})", "",
                     "Each file holds one entry as `{\"key\": value}`. Copy the value into the entry with the same key.",
                     "", "| Entry | Key | File |", "|---|---|---|"]
            for lab, key, fn in sorted(idx, key=lambda x: x[0].lower()):
                lab_s = lab.replace("|", "\\|")
                key_s = key.replace("|", "\\|")
                lines.append(f"| {lab_s} | `{key_s}` | [{fn}.json](<{fn}.json>) |")
            open(os.path.join(d, "INDEX.md"), "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
        rows.append([name, SECTIONS[name][0], SECTIONS[name][1], len(txt.encode("utf-8")), n_entries])

    prev = json.load(open(a.previous, encoding="utf-8")) if a.previous else None
    changed = {}
    if prev:
        for name in sorted(set(hashes["sections"]) | set(prev["sections"])):
            if hashes["sections"].get(name) == prev["sections"].get(name):
                continue
            new_e, old_e = hashes["entries"].get(name), prev["entries"].get(name)
            if new_e is not None and old_e is not None:
                added = [new_e[k]["name"] for k in new_e if k not in old_e]
                removed = [old_e[k]["name"] for k in old_e if k not in new_e]
                modified = [new_e[k]["name"] for k in new_e if k in old_e and new_e[k]["sha"] != old_e[k]["sha"]]
                changed[name] = {"added": added, "removed": removed, "modified": modified}
            else:
                changed[name] = None

    with open(os.path.join(ROOT, "SECTIONS.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(f"# Sections ({a.label})\n\n")
        f.write("Every section of the world, as one file in [`sections/`](sections/). The big sections are also split\n"
                "into one file per entry in [`entries/`](entries/). **content** and **settings** sections are safe to\n"
                "copy into your own save; leave **meta** sections alone.\n\n")
        f.write(f"| Section | Category | What it holds | Size | Entries | Changed in {a.label} |\n|---|---|---|---|---|---|\n")
        for name, cat, desc, size, n in rows:
            mark = "—" if not prev else ("**yes**" if name in changed else "no")
            link = f"[{name}](sections/{name}.json)"
            if n != "":
                link += f" · [entries](entries/{name}/INDEX.md)"
            f.write(f"| {link} | {cat} | {desc} | {size:,} B | {n} | {mark} |\n")

    json.dump(hashes, open(os.path.join(RELEASES_DIR, a.label + ".hashes.json"), "w", encoding="utf-8", newline="\n"),
              ensure_ascii=False, indent=1)

    with open(os.path.join(RELEASES_DIR, a.label + ".changes.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(f"# {a.label}: changed sections and entries\n\n")
        if not prev:
            f.write("Baseline release: every section is new to this repository.\n")
        elif not changed:
            f.write(f"No section changed since {prev['label']}.\n")
        else:
            f.write(f"Against {prev['label']}. Copy only these into your save.\n\n")
            for name, c in changed.items():
                f.write(f"## {name}\n")
                if c is None:
                    f.write(f"Whole section changed: copy [sections/{name}.json](../sections/{name}.json).\n\n")
                    continue
                for kind in ("added", "removed", "modified"):
                    if c[kind]:
                        f.write(f"- **{kind.capitalize()} ({len(c[kind])}):** " + "; ".join(sorted(c[kind])) + "\n")
                f.write("\n")

    files = {}
    for rel in ("world/MHA_Your_Story.json", "world/MHA_Your_Story.studio.json"):
        files[rel] = sha(open(os.path.join(ROOT, rel), encoding="utf-8").read())
    manifest = {"world": world.get("title"), "worldId": world.get("shortId"), "release": a.label,
                "published": a.published, "heroesVersion": G.get("heroesVersion"),
                "compatibilityRevision": G.get("compatibilityRevision"), "layout": "Voyage 2.52 (triggerDefinitions, parties)",
                "sections": len(S), "files": files}
    json.dump(manifest, open(os.path.join(ROOT, "MANIFEST.json"), "w", encoding="utf-8", newline="\n"),
              ensure_ascii=False, indent=2)
    print(f"release {a.label}: {len(S)} sections, {sum(len(v) for v in hashes['entries'].values())} entry files")
    if prev:
        print("changed sections:", ", ".join(changed) or "none")
        for name, c in changed.items():
            if c:
                print(f"  {name}: +{len(c['added'])} -{len(c['removed'])} ~{len(c['modified'])}")


if __name__ == "__main__":
    main()
