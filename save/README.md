# Save-ready sections (11.13)

Sections whose records need extra fields inside a running save. Paste these in the in-game State Editor, not
the plain files in `sections/`.

- [`npcs.json`](npcs.json): every NPC with the `"status": ""` field a save requires. Pasting the whole
  section also puts every NPC back at its home location and clears any status the story gave them
  (for example an injury). To keep those, update one NPC at a time instead (see UPDATE_GUIDE.md).
