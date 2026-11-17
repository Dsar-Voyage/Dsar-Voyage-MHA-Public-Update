# Release notes

Each published update lists the sections and entries it changed, so you can copy only those into your
save or remix (see the [README](README.md) for how). The machine-generated list for every release is in
[`releases/`](releases/).

---

## 11.17 — Bonds That Feel Like Bonds (published 2026-11-17)

People at Close and above sometimes take the first step when they share a scene with you (a gym invite, a saved seat,
a rematch); Trusted ones confide, come looking when you are hurt and take your side. An invitation, challenge or
reminder you ignore or decline comes back at most once that day, never as an order. A knocked-out or downed foe stays
flat even when you order them up. Recovery Girl's Errand completes once her errands and patient are handled and she has
told you something her healing costs or cannot do. No new scores, stages or romance mechanics.
Full per-entry list: [`releases/11.17.changes.md`](releases/11.17.changes.md).

| Section | What changed | Copy |
|---|---|---|
| `aiInstructions` | `generateNPCIntents` (MHA Initiative and Bonds: the FRIENDSHIP AND BONDS and ROMANCE parts, and the one-more-time rule). | whole `generateNPCIntents` entry |
| `triggerDefinitions` | `Combat: turning points` (downed and knocked-out foes stay flat when ordered up). The `Pack: load` / `Event Lazy: load` changes are only re-packed data loaders. | **Running save:** copy `Combat: turning points` into *parties → (your party) → triggers* ([UPDATE_GUIDE.md](UPDATE_GUIDE.md)) |
| `parties.quests`, `parties.questTriggers` | `Recovery Girl's Errand`: completion condition, objective and brief. | the quest's fields (keep its status) and its quest trigger |

---

## 11.16.1 — Patch: Training + Fair Fights (published 2026-11-16)

One training action is one drill or set unless the player asks for longer, and the body's toll follows Quirk Strain
(below 60, no broken bones from ordinary training): one line in `generateStory` > MHA Days and Parties. New characters
use the NPC health formula (health 200 at level 1, +20 per level; Endurance still adds on top); saves keep their own
maximum. Parting words ("See you later, Kirishima", "I'm heading off alone") take the named party members out of the
party, and a companion the story has not named for 5 turns goes their own way; a classmate in your room follows you only
when the story ties them to the move. A second stage-record guard runs right after the story, so "(Summer Training)"
copies never show for a turn. On move-in night the clock says Monday is the assessment and guidance only.
Full per-entry list: [`releases/11.16.1.changes.md`](releases/11.16.1.changes.md).

| Section | What changed | Copy |
|---|---|---|
| `triggerDefinitions` | Added `Party: parting and quiet companions`, `Record Guard: students (after the story)`; changed `Clock: Show Time`, the six `Follow: ... (before the story)` scripts. The `Pack: load` / `Event Lazy: load` changes are only re-packed data loaders. | **Running save:** copy the named entries into *parties → (your party) → triggers* ([UPDATE_GUIDE.md](UPDATE_GUIDE.md)) |
| `aiInstructions` | `generateStory` (MHA Days and Parties: training pace and the Path line). | whole `generateStory` entry |
| `resourceSettings` | Health: initial 200, +20 per level. Affects new characters only. | whole section (optional for running saves) |

---

## 11.16 — Day One + Fight Polish (published 2026-11-16)

No Battle Trial on day one: on Monday April 1 the clock note says the timetable does not run yet (no costumes, Hero
Studies, Ground Beta or trial), both day-2 plans say so, and the Courtyard's bus line applies on lesson days only. A
downed fighter cannot stand, reach for a weapon or crawl off, and is released once treated (5+ health) so they can
rejoin the party; "fight ... with NAME" keeps an ally on your team (only spar/duel/bout wording makes an opponent). A
"Quirk: Given Out" trait makes every use fizzle while the Quirk is out, Strain gained while out is taken back, health
lost to your own Quirk outside fights is refunded, and four Drawbacks call the give-out "its one give-out injury".
Fights stop closing every exchange on the same look or stance.
Full per-entry list: [`releases/11.16.changes.md`](releases/11.16.changes.md).

| Section | What changed | Copy |
|---|---|---|
| `triggerDefinitions` | `Clock: Show Time`, `Day Plan: day 2 [1-A]`, `Day Plan: day 2 [1-B]` (day one), `Combat: turning points`, `Combat: fight director`, `Combat: spar opponent leaves the party`, `Quirk: gives out at 100`, plus data loaders `Pack: load 72-74`. 10 changed. | **Running save:** copy the named entries into *parties → (your party) → triggers* ([UPDATE_GUIDE.md](UPDATE_GUIDE.md)) |
| `traits` | Added `Quirk: Given Out` (needed by the give-out trigger); `Drawback: Recoil`, `Overheating`, `Sensory Overload`, `Bodily Toll` reworded. | the added and modified entries |
| `resourceSettings` | Quirk Strain: nothing added while the Quirk is out; no health cost at 80+ or 100. | whole section |
| `locations` | U.A. Academy: the Courtyard's bus line (lesson days only). | field by field |

**Running saves already past Monday April 1** don't need the day-one changes.

---

## 11.15 — Polish + Izuku Fix (published 2026-11-15)

Downed fighters stay down (alive) until treated, and a downed party member leaves the party until they recover, which
ends the loop where Izuku was knocked out, revived at 1 health and knocked out again. A player's own self-breaking Quirk
costs Quirk Strain, never health; at 100 Strain it gives out once (one small injury, applied by a trigger) and fizzles
until Strain falls below 60. The USJ climax keeps canon timing; your own Battle Trial match plays over several turns,
round 5 ends, costumes show at Ground Beta; spars, referees and long fights read better; Dark Shadow stays with
Tokoyami; "skip to day 3" means the header's Day 3; healing works on titled names.
Full per-entry list: [`releases/11.15.changes.md`](releases/11.15.changes.md).

| Section | What changed | Copy |
|---|---|---|
| `triggerDefinitions` | 9 added: `Quirk: gives out at 100`, `Canon Beat: USJ climax clock`, `Clock: day numbers in the player's words`, six `Battle Trial: the player's match ...`. Changed: `Combat: turning points` (stays down, out of the party), `Combat: fight director`, `Combat: bout referee`, `Combat: healing scales`, `Battle Trial: round 5 ends ...`, `Companion: Dark Shadow`, `Clock: Skip Days`, `Day Plan: after a skip`, plus the data loaders (`Pack: load ...`, `Event Lazy: load ...`, `Prune: ...`, `Wardrobe: ...`). | **Remix:** replace the whole section. **Running save:** copy the added entries and `Combat: turning points` into *parties → (your party) → triggers* ([UPDATE_GUIDE.md](UPDATE_GUIDE.md)) |
| `resourceSettings` | Health is never deducted for the character's own Quirk; Strain is the Quirk's only cost. | whole section |
| `aiInstructions` | Drawback stages and Pushed Through in Action Resolution; a canon namesake's injuries never carry over; fight variety and referee pacing. | the modified entries |
| `parties.narrativeEvents`, `parties.quests`, `parties.questTriggers` | The USJ Attack beats; Battle Trial objective "with your team". | the modified entries |
| `npcs`, `storyStarts` | Vlad King referees quietly; the Sidekick start's commuter stays quiet. | the changed entries, field by field (never the whole section) |

**Running saves:** the Quirk fix needs both the new `resourceSettings` and the `Quirk: gives out at 100` trigger. A new
game is the clean way to get everything.

---

## 11.14 — PLUS ULTRA combat (published 2026-11-14)

A complete combat overhaul. Fights open on the ground and play out as wind-up, hit and cost; foes reach turning points
as they get hurt (Pressed, Last Stand, Down) and are knocked out, not killed, unless you clearly go for the kill; the
story follows you when you are badly hurt, go down and come back; a PLUS ULTRA limit break on the edge of a fight; an
optional Challenge setting (Story +8 or Plus Ultra -8, fights only); healing that scales in fights; Transformation
forms; teachers never attack students, sparring partners leave the party so their hits land, and referees stop bouts on
real health and stamina. Classes, conversations and everyday life are unchanged.
Full per-entry list: [`releases/11.14.changes.md`](releases/11.14.changes.md).

| Section | What changed | Copy |
|---|---|---|
| `triggerDefinitions` | 11 added, all named `Combat: ...` (turning points, fight director, player badly hurt, spar opponent leaves the party, bout referee, Plus Ultra surge and aftermath, challenge in fights, healing scales, Quirk form on and upkeep), plus the changed data loaders (`Pack: load ...`, `Event Lazy: load ...`) and `Mechanics: player training safety net`. 11 added, 73 changed. | **Remix:** replace the whole section. **Running save:** copy the `Combat: ...` entries into *parties → (your party) → triggers* ([UPDATE_GUIDE.md](UPDATE_GUIDE.md)) |
| `traits` | 7 added: `PLUS ULTRA: Surge`, `PLUS ULTRA: Overexerted`, `Challenge: Story`, `Challenge: Plus Ultra`, their two `(in a fight)` twins, `Quirk Form: Active`. | the 7 added entries (needed by the triggers above) |
| `traitCategories` | New optional `Challenge` group before Appearance Builder (character creation only). | new games only |
| `npcs` | Rank modifiers for pros, villains and students (damage, damage reduction, success bonus); Vlad King lets fighters work between calls when he referees. | the changed entries, field by field (never the whole section) |
| `abilities` | Move tiers rescaled (Technique, Special, Ultimate bonuses). | whole section for a remix; optional in a save |
| `combatSettings`, `progressionSettings` | Ability tiers and cooldowns (Techniques none, Special 2, Ultimate 5), an ability point every level. | whole section |
| `aiInstructions`, `gameModes` | Combat narration ("Combat Is the Engine's", "MHA Fights on Screen"), the In Combat intent rules, the fight-only teacher ban. | the modified entries |
| `successLevelSettings` | Fight beats for each roll tier (Wipeout turns the tide, Go Beyond! close-up, PLUS ULTRA! highlight). | whole section |
| `characterArchetypes` | An "In a fight:" line for each of the 22 archetypes. | the modified entries |
| `resourceSettings`, `encounterElements`, `storyStarts`, `parties.narrativeEvents` | Health usage wording, encounter tuning, the Sidekick start's streamer talks less, the USJ Nomu beat. | the modified entries |

**Running saves:** the Challenge setting is chosen at character creation, so an existing save plays the standard game
unless you add a `Challenge: ...` trait yourself. Stage rank changes reach NPCs already met only when their records are
updated. A new game is the clean way to get everything.

---

## Repository fix (2026-11-14): updating NPCs in a save
A player's State Editor refused an update with `npcs > ... > status: Expecting string` and
`characterArchetypes > ...: Expecting string ... got {"file": ...}`. Two causes: a running save's NPCs carry a
`status` field and include the people the story created, so the whole `npcs` section must never be pasted into a
save (update NPCs field by field); and a `releases/*.hashes.json` fingerprint file was pasted as if it were a
section (those files now say "NOT game data"). No world content changed: release 11.13 is the same. See the new
table in [UPDATE_GUIDE.md](UPDATE_GUIDE.md#if-the-editor-says-state-edit-did-not-save).

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
