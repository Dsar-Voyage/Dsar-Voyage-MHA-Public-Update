# Sections (11.12)

Every section of the world, as one file in [`sections/`](sections/). The big sections are also split
into one file per entry in [`entries/`](entries/). **content** and **settings** sections are safe to
copy into your own save; leave **meta** sections alone.

| Section | Category | What it holds | Size | Entries | Changed in 11.12 |
|---|---|---|---|---|---|
| [abilities](sections/abilities.json) · [entries](entries/abilities/INDEX.md) | content | Every Quirk technique and ability, with unlock levels and effects | 998,651 B | 1315 | no |
| [aiInstructions](sections/aiInstructions.json) · [entries](entries/aiInstructions/INDEX.md) | settings | Narrator and engine instruction blocks (story, NPCs, encounters, starts) | 296,182 B | 18 | **yes** |
| [attributeSettings](sections/attributeSettings.json) | settings | Attributes and their modifiers | 602 B |  | no |
| [authorSeeds](sections/authorSeeds.json) | content | Writing-style seeds for the narrator | 1,353 B |  | no |
| [characterArchetypes](sections/characterArchetypes.json) · [entries](entries/characterArchetypes/INDEX.md) | content | Templates for generated characters | 6,302 B | 22 | no |
| [characterCreationMusic](sections/characterCreationMusic.json) | settings | Music used during character creation | 10 B |  | no |
| [characterCreationSettings](sections/characterCreationSettings.json) | settings | Character creator steps and options | 74 B |  | no |
| [combatSettings](sections/combatSettings.json) | settings | Damage types and combat rules | 1,042 B |  | no |
| [compatibilityRevision](sections/compatibilityRevision.json) | meta | Voyage layout revision | 3 B |  | no |
| [death](sections/death.json) | settings | What happens when a character goes down | 3,851 B |  | no |
| [encounterElements](sections/encounterElements.json) · [entries](entries/encounterElements/INDEX.md) | content | Building blocks for generated encounters | 2,383 B | 14 | no |
| [endGame](sections/endGame.json) | settings | Ending narration | 916 B |  | no |
| [factions](sections/factions.json) · [entries](entries/factions/INDEX.md) | content | Hero agencies, the League, U.A. and other groups | 18,232 B | 11 | no |
| [gameModes](sections/gameModes.json) · [entries](entries/gameModes/INDEX.md) | content | Play modes and their narrator rules | 57,442 B | 5 | no |
| [gameplayMusicSettings](sections/gameplayMusicSettings.json) | settings | Gameplay music | 10,990 B |  | no |
| [heroesVersion](sections/heroesVersion.json) | meta | World schema version | 3 B |  | no |
| [imagePromptConfiguration](sections/imagePromptConfiguration.json) | settings | Image prompt routing for portraits and scenes | 13,705 B |  | no |
| [itemSettings](sections/itemSettings.json) | settings | Item categories, tiers and slots | 3,918 B |  | no |
| [itemTypes](sections/itemTypes.json) · [entries](entries/itemTypes/INDEX.md) | content | Every item: gear, costumes, food, documents, currency | 59,984 B | 87 | no |
| [locationArchetypes](sections/locationArchetypes.json) · [entries](entries/locationArchetypes/INDEX.md) | content | Templates for generated locations | 3,622 B | 11 | no |
| [locationSettings](sections/locationSettings.json) | settings | Location rules | 261 B |  | no |
| [locations](sections/locations.json) · [entries](entries/locations/INDEX.md) | content | Every place, its areas, pictures and hidden info | 696,570 B | 62 | no |
| [mods](sections/mods.json) | meta | Installed mods | 60 B |  | no |
| [nameFilterSettings](sections/nameFilterSettings.json) | settings | Name filter rules | 2,749 B |  | no |
| [narratorStyle](sections/narratorStyle.json) | settings | Narrator voice | 1,972 B |  | no |
| [npcTypes](sections/npcTypes.json) · [entries](entries/npcTypes/INDEX.md) | content | Types used for generated NPCs | 31,875 B | 15 | no |
| [npcs](sections/npcs.json) · [entries](entries/npcs/INDEX.md) | content | Every character: profiles, stages, looks and hidden info | 1,270,376 B | 295 | **yes** |
| [otherSettings](sections/otherSettings.json) | settings | Miscellaneous numbers | 87 B |  | no |
| [parties.arcs](sections/parties.arcs.json) | content | Long story arcs (inside Parties) | 3 B |  | no |
| [parties.narrativeEvents](sections/parties.narrativeEvents.json) · [entries](entries/parties.narrativeEvents/INDEX.md) | content | Canon events and side events (inside Parties) | 523,797 B | 214 | no |
| [parties.questTriggers](sections/parties.questTriggers.json) · [entries](entries/parties.questTriggers/INDEX.md) | content | Quest progress triggers (inside Parties) | 27,570 B | 54 | no |
| [parties.quests](sections/parties.quests.json) · [entries](entries/parties.quests/INDEX.md) | content | Every quest (inside Parties) | 89,558 B | 54 | no |
| [premadeCharacters](sections/premadeCharacters.json) | content | The premade player characters | 25,378 B |  | no |
| [progressionSettings](sections/progressionSettings.json) | settings | Levelling cadence | 1,467 B |  | **yes** |
| [randomNames](sections/randomNames.json) | content | Random name pools | 3,006 B |  | no |
| [realms](sections/realms.json) | content | The realm (Japan) | 1,012 B |  | no |
| [regionArchetypes](sections/regionArchetypes.json) · [entries](entries/regionArchetypes/INDEX.md) | content | Templates for generated regions | 8,506 B | 23 | no |
| [regions](sections/regions.json) · [entries](entries/regions/INDEX.md) | content | Map regions | 457,859 B | 161 | no |
| [relationshipStages](sections/relationshipStages.json) | settings | Relationship stages | 798 B |  | no |
| [resourceSettings](sections/resourceSettings.json) | settings | Health, Stamina and Strain | 6,123 B |  | **yes** |
| [skillSettings](sections/skillSettings.json) | settings | Skill rules | 641 B |  | **yes** |
| [skills](sections/skills.json) · [entries](entries/skills/INDEX.md) | content | Every skill | 23,361 B | 66 | no |
| [storySettings](sections/storySettings.json) | settings | Story settings | 9,572 B |  | no |
| [storyStarts](sections/storyStarts.json) · [entries](entries/storyStarts/INDEX.md) | content | Every story start | 124,493 B | 17 | no |
| [successLevelSettings](sections/successLevelSettings.json) | settings | Success level narration | 2,488 B |  | no |
| [tipSettings](sections/tipSettings.json) | settings | Loading tips | 2,029 B |  | no |
| [traitCategories](sections/traitCategories.json) · [entries](entries/traitCategories/INDEX.md) | content | Trait categories (Paths, Quirk families, backgrounds ...) | 67,738 B | 17 | no |
| [traits](sections/traits.json) · [entries](entries/traits/INDEX.md) | content | Every trait: Paths, Quirks, backgrounds and their narrator rules | 1,395,634 B | 1139 | no |
| [triggerDefinitions](sections/triggerDefinitions.json) · [entries](entries/triggerDefinitions/INDEX.md) | content | Every trigger: the clock, skips, events, wardrobe, travel ... | 2,503,931 B | 896 | **yes** |
| [worldLore](sections/worldLore.json) · [entries](entries/worldLore/INDEX.md) | content | World lore entries | 107,165 B | 93 | no |
| [worldVoices](sections/worldVoices.json) · [entries](entries/worldVoices/INDEX.md) | settings | Voice assignments | 65,567 B | 147 | no |
