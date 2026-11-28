# Release notes

Each published update lists the sections and entries it changed, so you can copy only those into your
save or remix (see the [README](README.md) for how). The machine-generated list for every release is in
[`releases/`](releases/).

---

## 11.28 — Outfits Fixed (published 2026-11-28, draft 901)

The portrait wardrobe rebuilt: the six "Wardrobe: group N" triggers no longer skip people their own record says are
dressed right (a stale record left people in the wrong clothes), write one record per person per pass (the engine
keeps at most 10 effects per trigger; four stage records per student used to hit that cap after about two people, so
most of a class never changed, e.g. gym icons all Move-In Night), and do a full pass on every move so people outside
the scene are dressed for their own place. New after-the-story copies run once the story has moved the party, so
outfits change on the arrival turn, and Campus Schedule copies run after a skip so everyone is placed first. Izuku's
base and Sports Festival records are elite tier (a strong NPC died instantly at 0 HP from his own Quirk). Outfit
traits no longer name wings, tails or extra arms (the narrator gave a player four arms).
Full per-entry list: [`releases/11.28.changes.md`](releases/11.28.changes.md).

| Section | What changed | Copy |
|---|---|---|
| `triggerDefinitions` | Changed: Wardrobe: group 1-6. New: Wardrobe: group 1-6 (after the story), Campus Schedule: 1A-1 / 1A-2 / 1B-1 / 1B-2 / faculty-1 / faculty-2 / campus (after a skip). | whole entries |
| `npcs` | Izuku Midoriya, Izuku Midoriya (Sports Festival): tier elite. | the tier field only |
| `traits` | The 20 "Outfit - ..." appearance traits: one line reworded. | whole entries |

**Outfits stuck in an old save:** copy the 12 `Wardrobe: group N` entries (with and without "(after the story)") and
the 7 `Campus Schedule: ... (after a skip)` entries from `entries/triggerDefinitions/`.

---

## 11.27 — Unstable Quirks and Custom Drawbacks (published 2026-11-27, draft 895)

New Quirk Strength "Unstable Quirk" (Power +1, Quirk Output +15, Quirk Control -10; unrestrained uses overshoot, with a
per-turn narrator note) and "Drawback: Custom" for Custom Quirks (the Quirk paragraph's "Drawback:" line is the cost,
shown after every use). Knocked-out foes are taken away by police, medics or their own crew, or kept down when the
player restrains them, also when the engine tags them "Dead". Talk turns move the clock a few minutes and an ordered
silence jumps to the next beat. Mentioning a place in talk or plans no longer moves the party. Strangers learn the
player's name, Quirk and limits only from an introduction, a file or what they saw; calming and sleep Quirks are
registered Quirks, not crimes; a player is only called spent at low Stamina or high Strain; a rest order ends three
in-game days after it was given.
Full per-entry list: [`releases/11.27.changes.md`](releases/11.27.changes.md).

| Section | What changed | Copy |
|---|---|---|
| `traits` | New: Unstable Quirk, Drawback: Custom. | new entries |
| `traitCategories` | Quirk Strength and Quirk Drawback list the new options. | whole entries |
| `aiInstructions` | generateStory Character Behavior (knowledge of the PC), generateActionInfo MHA Checks and Quirk Judgment (honest cost, mind-touching Quirks), summarization MHA Continuity Ledger (rest orders end). | whole entries |
| `triggerDefinitions` | New: Quirk: Unstable overshoot, Quirk: Custom Drawback shown. Changed: Combat: knocked-out foes taken away, Clock: Time Line Note, Travel: resolve place, Mechanics: Quirkless cleanup, and the Pack/Event loaders. | whole entries |

**Teleporting when you mention a place, in an old save:** copy `Travel: resolve place` from `entries/triggerDefinitions/`.
**Class time stuck at one minute per turn:** copy `Clock: Time Line Note`.

---

## 11.25.1 — Clubs! (published 2026-11-25, draft 881)

U.A. clubs on the canon cast: 11 clubs (Kendo/Itsuka Kendo, Light Music/Kyoka Jiro, Choir/Ibara Shiozaki, Robotics/Mei
Hatsume, Cooking/Rikido Sato, Tea Ceremony/Momo Yaoyorozu, Manga/Manga Fukidashi, Track and Field/Tenya Iida,
Swimming/Tsuyu Asui, Basketball/Tetsutetsu Tetsutetsu, Volleyball/Nejire Hado), each with a club trait card (+5 to its
skill), join and leave triggers (U.A. students, at most two clubs), a club-day reminder and practice that trains the
skill (+1 every third practice day) and the bond with the lead; 11 member-only club side events. The Wardrobe releases
a side-event outfit pause once that event is no longer active (portraits stuck in the wrong clothes). Canon students
and pros outside a fight are never dropped below half health or marked dead. New scripts are gated so they only run
with work.
Full per-entry list: [`releases/11.25.1.changes.md`](releases/11.25.1.changes.md).

| Section | What changed | Copy |
|---|---|---|
| `traits` | 11 new club cards ("Club: Kendo" ...). | new entries |
| `worldLore` | New: U.A. Clubs. | new entry |
| `narrativeEvents` (parties) | 11 new club side events. | new entries |
| `triggerDefinitions` | New: Club: join / leave / practice day / practice, the health floor triggers, the club events' start/resume/lapse/cast triggers. Changed: Wardrobe groups 1-6 (stuck-outfit release), Training: progress shows, side-event dispatchers and loaders. | whole entries |

**Stuck portraits in an old save:** copy the six `Wardrobe: group N` entries from `entries/triggerDefinitions/`.

---

## 11.25 — Voices & Limits (published 2026-11-25, draft 870)

The Quirk Strain limit grows with level: 100 at level 1, +10 per level, at most 300. Every Strain threshold is a share
of the limit (Drawback from 60%, 50% Exceptional; active from 80%; gives out at the limit), a level-up no longer adds
Strain, and a missed roll below the limit misfires instead of giving out. Knocked-out villains and unnamed foes stop
the fight: restrained or questioned foes stay down in the player's hands, otherwise police or medics take them away
(villain players: their own people). Every Class 1-A/1-B student, pro, teacher and 31 side characters have rewritten
personalities (Wants/Fears, Early bond, Devoted bond, a speaking sample); all 16 story starts have new opening scenes
(10 with condensed quest guidance to fit the 8,000-character limit). Authored NPCs no longer carry visualDescription
(their portraits exist; looks stay in basicInfo). generateStory gains a Living Cast rule.
Full per-entry list: [`releases/11.25.changes.md`](releases/11.25.changes.md).

| Section | What changed | Copy |
|---|---|---|
| `npcs` | 255 rewritten personalities; visualDescription emptied on all 299 authored records (12 gain an Appearance line in basicInfo). | whole entries |
| `storyStarts` | All 16 openings; quest guidance on 10. | whole entries |
| `resourceSettings` | Quirk Strain grows 10 per level; Strain and health rules in shares of the limit. | whole section |
| `traits` | Drawback texts in shares of the limit (17), All For One's Gift. | whole entries |
| `triggerDefinitions` | New: Combat: knocked-out foes taken away. Changed: Combat: turning points, Quirk: gives out at 100, Clock: Show Time, loaders. | whole entries |
| `aiInstructions` | Story (Living Cast), action, intents and item rules. | whole entries |

---

## 11.24 — Tougher Fights & Fixes (published 2026-11-24, draft 856)

Every NPC has about 55-60% more health (30 per level + 300 base) and stamina starts at 150 plus 5 per Endurance point,
grows 5 per level and recovers 8 per turn. Izuku's own One For All breaks are one minor injury at most and never mark
him dead. Tiny Quirk uses (a candle, a spark, a glow) cost no Strain. Robots, drones and machines break at 0 health.
Openings land in the right homeroom or course classroom; course classes hold their own students; the player's looks
never show up on classmates. Loss of Control runs wild at the limit before it gives out. Classmates left on the
Athletics Field go back to their school-uniform portraits. Skips to the camp, license exam or festivals move the
calendar with the story. Only one Midnight. Gelatinous Guardian no longer fixes the player's parents.
Full per-entry list: [`releases/11.24.changes.md`](releases/11.24.changes.md).

| Section | What changed | Copy |
|---|---|---|
| `otherSettings` | NPC health per level and base. | whole section |
| `resourceSettings` | Stamina (150, +5 per level, 8 per turn) and the Health / Quirk Strain rules (trivial uses, NPC backlash). | whole section |
| `attributeSettings` | Endurance adds 5 stamina per point. | whole section |
| `triggerDefinitions` | New: Clock: Skip unclear. Changed: Clock: Show Time, Combat: turning points, Opening: place from narration, Quirk: gives out at 100, Wardrobe groups 1-6, loaders. | whole entries |
| `aiInstructions` | `generateActionInfo` (Strain costs), `generateNPCUpdates` (damage details), `generateNewNPC` (one Midnight). | whole entries |
| `traits` | Gelatinous Guardian Quirk. | whole entry |

---

## 11.22 — New Quirks & Fixes (published 2026-11-23, draft 831)

Seven new Quirk families (Chain, Ricochet, Smoke Body, Draconic and the fusions Blackflame, Sandstorm, Ironwood) with
their techniques. Students get a monthly allowance on the 1st by Upbringing, plus a new Struggling Family upbringing.
Civilians, sidekicks and pros have their own apartment ("I walk home"). Eri smiles after the School Festival. Private
moments stay private, reports hold only the player's words, and asking someone to do something leaves it to them.
Gym-uniform changes no longer empty the scene. The Quirk Assessment runs all eight of the player's events before the
ranking. Write Your Own openings land at the right place and time. Backstory generation no longer trips the blocked-words
filter; Quirk Strain only comes from Quirk use; looking at a menu never orders.
Full per-entry list: [`releases/11.22.changes.md`](releases/11.22.changes.md).

| Section | What changed | Copy |
|---|---|---|
| `abilities` | 91 new techniques for the seven new Quirks. | new entries |
| `traits` / `traitCategories` | New Quirk families, Gifted variants and Struggling Family; Upbringing cards show the allowance; Drawback and course text. | whole entries |
| `triggerDefinitions` | New: Character: Eri grows, Money: Student Allowance, Opening: place from narration, Travel: my home. Changed: Quirk Assessment beat, Clock: Show Time and Clock: Start, changing rooms, loaders. | whole entries |
| `aiInstructions` | Story, action, opening, background, intents, items and learned-ability rules. | whole entries |
| `locations` | Musutafu Station District gains the area Your Apartment. | whole entry |
| `resourceSettings` | Quirk Strain rules. | whole section |

---

## 11.21.1 — Earned Reactions (published 2026-11-20, draft 797)

Reactions match the deed: ordinary acts (a nod, taking a seat, a decent drill) get ordinary reactions, never praise or
awe; strangers in the first days are curious or wary; praise is rare and earned.
Full per-entry list: [`releases/11.21.1.changes.md`](releases/11.21.1.changes.md).

| Section | What changed | Copy |
|---|---|---|
| `aiInstructions` | `generateStory` (Character Behavior), `generateDialogue` (MHA Dialogue), `generateNPCIntents` (MHA Reading the Player). | whole entries |

---

## 11.21 — First Day Fixes (published 2026-11-20, draft 796)

First Day at U.A. opens on Day 2, Monday April 1, in the morning again (when the opening room was not reported on the
first turn, the clock fell back to move-in evening), and the clock start writes its day and band so the next turn can't
slip back to Day 1. The first-day scene in 1-A plays its canon beats: Bakugo sneers "Deku", Iida introduces himself to
Izuku and admits he misjudged him, Uraraka arrives last behind Izuku. Looking at, checking or opening an item in a shop
never buys it. A new ability needs a successful Special Move Training roll or the same new trick practiced on earlier
turns (a one-off improvised move no longer becomes an ability). The narrator's teasing example no longer pairs Jiro and
Denki. Place art points at the re-approved images.
Full per-entry list: [`releases/11.21.changes.md`](releases/11.21.changes.md).

| Section | What changed | Copy |
|---|---|---|
| `triggerDefinitions` | Changed `Clock: Start` (only matters for a new game), `Clock: Show Time`, the eight `Items: shop [...]` triggers (one new condition each). The `Place Light:` and `Pack: load` changes are image links and re-packed data loaders: optional. | **Running save:** copy `Clock: Show Time` and the `Items: shop [...]` entries into *parties → (your party) → triggers* ([UPDATE_GUIDE.md](UPDATE_GUIDE.md)) |
| `aiInstructions` | `ItemGenerationAndUsage` (looking is not buying), `generateLearnedAbilities` (when to propose an ability), `generateStory` and `generateDialogue` (teasing line). | whole entries |
| `storyStarts` | `First Day at U.A.` (new games only). | not needed for a running save |

---

## 11.20 — Night Owls & Special Moves (published 2026-11-20, draft 789)

Special Moves work again: Voyage now files learned moves under the first tier, so every learned move is a Special Move
(+10, 2-turn cooldown; the `special` tier reads "Special Move ★"), Special Move Training creates
"Special Move: <name>" and recharges in 6 turns (was 30), and its card explains the 6-turn window between new moves.
The character creator's background explains the Quirk and leaves the Drawback to its trait (no invented costs), in
exactly five paragraphs with no headings. Clock: past midnight the date holds until sleep, dawn (5 a.m.) turns the day
for an all-nighter, one sleep is one day even after midnight, and naps or "before turning in" never move the day.
Skips wait during the Quirk Assessment and the player's own Battle Trial round and stop for the Media Break-In; skip to
a time shows that time. The Sports Festival runs on a schedule. Other courses go to their own homeroom; move-in night
names the player's room; Days 4-5 know whether the player fought in the Battle Trial. Narrator: vague errands never
buy anything, the player stays where a shift or errand ends, questions wait for the player's answer, paperwork never
makes a quest. Gear never changes a bar's maximum. Moving Day (An Ordinary Life) starts in the morning. Lighter
scripts on the heaviest turns (Dark Shadow, quest bonds, event cleanup).
Full per-entry list: [`releases/11.20.changes.md`](releases/11.20.changes.md).

| Section | What changed | Copy |
|---|---|---|
| `triggerDefinitions` | Added 8 (`Battle Trial: done (Class 1-A/1-B)`, `Battle Trial: missed (Class 1-A/1-B)`, `Clock: Skip waits for class exercises` (place it right before `Clock: Skip Days`), `Dorms: the player's room on move-in night (Class 1-A/1-B)`, `Festival: the day's schedule`); changed `Bonds: quest rewards stay small`, `Clock: Calendar 1`, `Clock: Show Time`, `Clock: Skip Band`, `Clock: Skip Days`, `Clock: Sleep`, `Clock: Time Line`, `Clock: Time Line Note`, `Companion: Dark Shadow`, `Prune: done dispatcher 1/2`, `Prune: path dispatcher 1/2`, `Side Event: starts 1`, the three `Travel: my homeroom (...)`, `Year So Far`. The `Pack: load` / `Event Lazy: load` changes are only re-packed data loaders. | **Running save:** copy the named entries into *parties → (your party) → triggers* ([UPDATE_GUIDE.md](UPDATE_GUIDE.md)); never re-add one-shot triggers your save already ran |
| `combatSettings` | Learned-move tiers: `technique` = "Special Move" (+10, cooldown 2), `special` = "Special Move ★" (+10, cooldown 2). Already-learned moves pick up the new values. | whole section |
| `abilities` | `Special Move Training`: cooldown 6, card text. | the `Special Move Training` entry |
| `aiInstructions` | `generateCharacterBackground` (two fields, five paragraphs, the Quirk paragraph explains the Quirk and adds no costs), `generateLearnedAbilities` (the Special Move rules now live in `custom`), `ItemGenerationAndUsage` (gear never changes a bar's maximum). | whole entries |
| `storySettings` | `questGenerationGuidance`: admin work never creates, advances or completes a quest. | whole section |
| `parties.quests` / `parties.questTriggers` | `First Patrol Report` fits a sidekick's first day. | the `First Patrol Report` entries (keep your quest status) |
| `npcs`, `locations`, `premadeCharacters` (and image links inside triggers) | Image links only: 514 images were re-approved under the production world for Voyage 2.60.3's publish check. Same pictures; the old links keep working. | **optional**: no need to copy into a running save |

## 11.18 — Friends Who Show Up (published 2026-11-18, draft 754)

Close friends come by once a day in free time (a knock or a text, never in class, fights or events). Heights Alliance
follows Aizawa's canon floor plan with door numbers for every student (Class 1-B's numbers are the world's own; canon
has no 1-B plan), and General Studies, Support and Management students live, cook and study in their own halls. Clock:
move-in night stays Sunday, one sleep = one day, a Write Your Own opening can name its start date, and the Battle Trial
hold lets go after three held turns. Training shows measurable results and every third counted day on a skill raises it
one level. Finished quests no longer leap a bond (the engine's +15 is trimmed to +4 / +1). New drawback: Emotional
Swing. New people's Quirks have limits instead of default pain. The narrator never plays the player character. Items
used up count once; quests close when really done; unnamed foes stay down. Smarter narration: the narrator style and
the story task's turn structure were merged with Kokey [BIFS]'s template (who is here, turn boundaries, character
behavior). Animals can die: a person at zero health is down, an animal at zero health is dead, and the knockout
safety no longer brings an animal foe back on 1 HP.
Full per-entry list: [`releases/11.18.changes.md`](releases/11.18.changes.md).

| Section | What changed | Copy |
|---|---|---|
| `triggerDefinitions` | Added 19 (`Bonds: a close friend comes by`, `Bonds: quest rewards stay small`, `Clock: Battle Trial release`, `Clock: Your Own Start Date`, `Combat: animals stay dead` (place it right after `Combat: turning points`), `Combat: the downed stay down`, `Dorms: room map note`, the three `Housing: ... player's places`, `Scene: changing rooms keep sides`, `Scene: dorms keep their class`, `Training: progress shows`, the three `Travel: my homeroom (...)` and three `Travel: my kitchen (...)`); changed `Canon Beat: The First-Day Quirk Assessment`, `Clock: Date Sync`, `Clock: Show Time`, `Clock: Skip Days`, `Clock: Sleep`, `Clock: Start`, `Combat: turning points`, `Mechanics: Quirkless cleanup`, `Prune: path dispatcher 1/2`, `Travel: leave (U.A.)`. The `Pack: load` / `Event Lazy: load` changes are only re-packed data loaders. | **Running save:** copy the named entries into *parties → (your party) → triggers* ([UPDATE_GUIDE.md](UPDATE_GUIDE.md)); never re-add one-shot triggers your save already ran |
| `narratorStyle` | Merged narrator style (Kokey [BIFS]'s template plus ours). | whole section |
| `aiInstructions` | 12 tasks: WORLD RULES (housing, Quirk limits) in all copies, `generateStory` (merged turn structure, who is here, turn boundaries, character behavior; Player Agency, dialogue order, no faux profundity), `generateNewNPC` / `generateNPCDetails` (limits, not default pain), `generateNPCUpdates` (quest-sized bond gains; zero health = dead for animals), `ItemGenerationAndUsage` (one use, one unit). | whole entries |
| `locations` | `U.A. Academy`: dorm areas (room numbers, wing maps, Dorm Rooms plan, Your Dorm Room), separate 1-A/1-B kitchens, new `Other Course Common Kitchen`. | the `U.A. Academy` entry |
| `npcTypes` | `Animal`: an animal brought to zero health dies. | the `Animal` entry |
| `traits`, `traitCategories` | Added `Drawback: Emotional Swing`; `Quirk Drawback` group lists it and notes which drawbacks are limits. | both entries |
| `parties.quests`, `parties.questTriggers` | `Giran's Supply Run`, `Paying the Broker`, `Power Loader's First Assignment` (completion), `The First Lecture` (Tuesday). | the quests' fields (keep status) and their quest triggers |
| `storySettings`, `storyStarts`, `worldLore` | Quest generation guidance (bond rewards); `Write Your Own` card (start date); `Heights Alliance Dorms` (room plan). | whole entries |

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
