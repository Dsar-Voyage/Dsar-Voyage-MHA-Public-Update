# Release notes

Each published update lists the sections and entries it changed, so you can copy only those into your
save or remix (see the [README](README.md) for how). The machine-generated list for every release is in
[`releases/`](releases/).

---

## Repository fix (2026-11-14): save-ready NPCs
A player's State Editor refused an update with `npcs > ... > status: Expecting string` and
`characterArchetypes > ...: Expecting string ... got {"file": ...}`. Two causes, both fixed in the guide:
running saves need a `status` field on every NPC (new: [`save/npcs.json`](save/npcs.json)), and the
`releases/*.hashes.json` fingerprint files were pasted as if they were sections (they now carry a "NOT game data"
note). No world content changed: release 11.13 is the same. See the new table in
[UPDATE_GUIDE.md](UPDATE_GUIDE.md#if-the-editor-says-state-edit-did-not-save).

## 11.13 — Dark Shadow, the lottery and tougher NPCs (published 2026-11-13)

Dark Shadow as his own character with his own art, a Battle Trial lottery that can give a fair 2v2, skips that never
replay an event you already played, NPCs with about 2.6x the health, a school timetable, upper-year generated students,
Quirk questions asked once, and changing rooms that stay separate.
Full per-entry list: [`releases/11.13.changes.md`](releases/11.13.changes.md).

| Section | What changed | Copy |
|---|---|---|
| `triggerDefinitions` | **Battle Trial lottery** (`Battle Trial: lottery` and the `[2v2 ...]` round, rule and Day Plan variants), **skips never replay** (`Quest Close: ...`, 5 added), **Dark Shadow** (`Companion: Dark Shadow`, `Portrait Swap: Dark Shadow (...)`, `Wardrobe: group 1`-`6`), **changing rooms** (`Scene: changing rooms (...)`), the timetable and Quirk-question rules (`Clock: Show Time`), and the data loaders they read (`Pack: load ...`, `Event Lazy: load ...`). 41 added, 94 changed. | **Remix:** replace the whole section. **Running save:** copy the listed entries one by one into *parties → (your party) → triggers* ([UPDATE_GUIDE.md](UPDATE_GUIDE.md)) |
| `npcs` | **Dark Shadow** and his three stage records (`(Festival Arc)`, `(Summer Arc)`, `(License Arc)`). | the 4 added entries |
| `otherSettings` | NPC health: 20 per level + 180 (was 8 + 66). | whole section |
| `aiInstructions` | Generated people get a want, a concrete Quirk and a voice; generated Hero Course students are upper-years; never a second Dark Shadow (`generateNewNPC`). | 1 modified |
| `npcTypes` | Hero Course Student: generated ones are second- or third-years. | 1 modified |
| `worldLore` | The weekday timetable with times. | 1 modified |

**Running saves:** the lottery rolls on Day 2 or earlier, so a save already past that keeps the old 3v2. NPCs already
met keep their old health until the engine recalculates them; a new game is the clean way to get the new pools.

---

## 11.12 — Fixes and level caps (published 2026-11-12)

Level caps by time of year and much slower leveling, "I leave" that works, no duplicate heroes when the story uses a
real name, healed injuries that stay healed, items and bets that behave, and a Quirk Strain guard.
Full per-entry list: [`releases/11.12.changes.md`](releases/11.12.changes.md).

| Section | What changed | Copy |
|---|---|---|
| `triggerDefinitions` | **Level caps** (`Mechanics: level cap ...`, 20 added: the caps per period, the Path flags), **leaving rooms** (`Travel: leave (U.A.)`, `Travel: leave (elsewhere)`), the Strain guard and room memory (`Clock: native sync`, `Clock: native follow`), the third skip ask and date fixes (`Clock: Skip Days`, `Clock: Date Sync`), healed injuries, declined bets and food offers (`Clock: Show Time`), and the calendar data they load (`Pack: load 72`-`74`). 22 added, 8 changed. | **Remix:** replace the whole section. **Running save:** copy the listed entries one by one into *parties → (your party) → triggers* ([UPDATE_GUIDE.md](UPDATE_GUIDE.md)) |
| `npcs` | 33 heroes and villains get `properName` (their real name), so the story using it no longer creates a duplicate. | the 33 modified entries |
| `aiInstructions` | Two names for one person (`generateNewNPC`), items kept and crafting (`ItemGenerationAndUsage`), room contents, settled bets and healed injuries (`summarization`). | 3 modified |
| `progressionSettings`, `skillSettings` | Slower leveling: level 2 costs 1,000 XP (+300 per level), skills 100 + 40 per level, less XP per skill upgrade, new skill and new place. | whole section (each) |
| `resourceSettings` | One line in Quirk Strain's rules: a turn adds at most +25 (+37 Exceptional, +60 two Gifted). | whole section |

**Running saves:** the level caps also need storage `studentStage` (a save past the Sports Festival already has it).
The new XP curve applies to levels you gain from now on.

---

## 11.11 — Play the story (published 2026-11-11)

29 new canon moments, skips that stop for every canon event, a clock that follows the story's own time line,
Miss Midnight, private scenes that stay private, recovery that clears you, the Slipstream Fusion Quirk, and fixes.
Full per-entry list: [`releases/11.11.changes.md`](releases/11.11.changes.md).

| Section | What changed | Copy |
|---|---|---|
| `triggerDefinitions` | The skip, calendar and clock system (skips stop at canon events, the closing time line, Date Sync, waking at home), 29 new side-event starts and wraps, Miss Midnight, private sessions, Room King, wardrobe (Shinso). 63 added, 10 removed, 311 changed. | **Remix:** replace the whole section. **Running save:** copy the listed entries one by one into *parties → (your party) → triggers*, never the whole section (see [UPDATE_GUIDE.md](UPDATE_GUIDE.md)); with this many changes, a new game is easier |
| `parties.narrativeEvents` | 29 new canon moments (G1-G29) added; 15 events adjusted. | the 29 added + 15 modified entries |
| `npcs` | **Midnight is now "Nemuri Kayama"** (the old `Midnight` record is removed and a new one added: replace it, don't keep both). Shinso's looks, festival and camp stage records, Present Mic, Nezu, Recovery Girl. | 1 added, 1 removed, 9 modified |
| `traits` | Slipstream Fusion Quirk added; Class 1-A/1-B "Quirkless" wording; Path texts. | 1 added, 16 modified |
| `abilities` | The 11 Slipstream techniques. | 11 added |
| `aiInstructions` | Who knows what, recovery, day count, time pacing (`generateStory`, `generateNPCUpdates`, `summarization`, `generateActionInfo`, `generateLearnedAbilities`). | 5 modified |
| `worldLore`, `storyStarts`, `gameModes`, `locations`, `factions`, `npcTypes`, `traitCategories`, `worldVoices`, `parties.quests`, `parties.questTriggers` | Miss Midnight's name, schedule notes, U.A. and stadium details, the new Fusion family. | modified entries only |
| `attributeSettings` | Voyage's own format change (a stat modifier stored as a list; same values). | whole section |
| `compatibilityRevision` | Meta: Voyage layout revision. | **do not copy** |

**Best on a new game:** this update rebuilt the skip and clock triggers; a save in progress can take them entry by
entry ([UPDATE_GUIDE.md](UPDATE_GUIDE.md)), but canon moments whose day has already passed won't start.

---

## 11.02 — baseline (published 2026-11-05)

The first release in this repository: the full world as published in Patch 11.02. Every section is new
here; use it as the starting point for later updates.

Patch 11.02 highlights: the **One of the League** start, buyable outfits and exact shop prices, item
tiers, clock fixes (time no longer runs ahead, stated times move the header, Midnight the teacher isn't
the hour), the trigger-run Battle Trial with the Ground Beta Monitoring Room, training-ground entrances,
recovery within three days, and nobody dies at Hosu.

- Sections: all 51 (see [`SECTIONS.md`](SECTIONS.md)).
- Machine list: [`releases/11.02.changes.md`](releases/11.02.changes.md).
