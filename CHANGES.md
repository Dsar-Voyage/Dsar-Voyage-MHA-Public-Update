# Release notes

Each published update lists the sections and entries it changed, so you can copy only those into your
save or remix (see the [README](README.md) for how). The machine-generated list for every release is in
[`releases/`](releases/).

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
