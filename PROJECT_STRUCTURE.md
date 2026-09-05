# Project Structure

This repository is organized so the app code, tests, and documentation have clear responsibilities.

## Current Layout

```text
.
|-- guitarChordsViewer.py
|-- src/
|   `-- guitar_chords_viewer/
|       |-- __init__.py
|       |-- app.py
|       |-- fretboard.py
|       |-- music_theory.py
|       |-- playability.py
|       `-- ui_tkinter.py
|-- tests/
|   |-- test_fretboard.py
|   |-- test_music_theory.py
|   `-- test_playability.py
|-- skills/
|   |-- guitar-chord-playability/
|   |   |-- SKILL.md
|   |   `-- agents/
|   |       `-- openai.yaml
|   `-- markdown-doc-dedup/
|       |-- SKILL.md
|       `-- agents/
|           `-- openai.yaml
|-- AGENTS.md
|-- DESIGN_PRINCIPLES.md
|-- DESIGN_PRINCIPLES_CHECKLIST.md
|-- PROJECT_STRUCTURE.md
|-- SCRIPT_FEATURES.md
|-- SETUP_CHECKLIST.md
|-- README.md
`-- LICENSE
```

## Source Code

### `guitarChordsViewer.py`

Root-level launcher.

Keep this file small. It should only prepare the local import path and call the package entry point. Run commands are maintained in `SETUP_CHECKLIST.md`.

### `src/guitar_chords_viewer/app.py`

Application entry point.

Use this file for the `main()` function that creates and runs the desktop app.

### `src/guitar_chords_viewer/music_theory.py`

Music data and pure calculation logic.

Use this file when changing:

- root notes
- string tuning
- chord qualities
- drop voicing shapes
- fret-position calculation

This file should not import `tkinter`.

### `src/guitar_chords_viewer/fretboard.py`

Fretboard drawing constants and coordinate helpers.

Use this file when changing:

- colors
- marker sizes
- canvas margins
- fret and string coordinate helpers

This file should not contain chord formulas.

### `src/guitar_chords_viewer/playability.py`

Physical guitar-grip rules.

Use this file when changing:

- playable/stretchy/not recommended thresholds
- fret-span rules
- open-string playability handling
- maximum recommended fret position

This file should not contain chord formulas or UI drawing code.

### `src/guitar_chords_viewer/ui_tkinter.py`

Native desktop UI.

Use this file when changing:

- window behavior
- dropdown controls
- event handling
- canvas rendering calls
- status text

This file can depend on `music_theory.py` and `fretboard.py`.

## Tests

### `tests/test_music_theory.py`

Unit tests for pure music calculation behavior.

Use this file when changing `music_theory.py`.

### `tests/test_playability.py`

Unit tests for physical guitar-grip rules.

Use this file when changing `playability.py`.

### `tests/test_fretboard.py`

Unit tests for fretboard coordinate helpers.

Use this file when changing `fretboard.py`.

Test commands are maintained in `SETUP_CHECKLIST.md`.

## Skills

### `skills/markdown-doc-dedup/`

Repository copy of the Markdown duplication-check skill.

Use this folder to share the skill with other agents or machines.

To reuse it elsewhere, copy `skills/markdown-doc-dedup/` into that agent's skills directory, or have the agent read `skills/markdown-doc-dedup/SKILL.md` directly.

### `skills/guitar-chord-playability/`

Repository copy of the guitar chord playability skill.

Use this folder to share the playability rules with other agents or machines. To reuse it elsewhere, copy `skills/guitar-chord-playability/` into that agent's skills directory, or have the agent read `skills/guitar-chord-playability/SKILL.md` directly.

## Documentation

Documentation files live at the repository root. Their individual intentions are documented in `AGENTS.md`.

## Update Rule Of Thumb

- Change music behavior in `music_theory.py`.
- Change drawing measurements or colors in `fretboard.py`.
- Change user interaction in `ui_tkinter.py`.
- Change startup behavior in `app.py` or `guitarChordsViewer.py`.
- Add tests under `tests/`.
