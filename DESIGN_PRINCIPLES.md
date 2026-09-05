# Design Principles And Recommended Architecture

This guide explains practical software design principles for maintaining `guitarChordsViewer.py` and recommends a simple architecture for future updates.

## Design Principles

### SOLID

SOLID is a set of object-oriented design principles. For this app, use them lightly.

- Single Responsibility Principle: each function or class should have one clear reason to change.
- Open/Closed Principle: add new chord qualities or tunings by extending data structures when possible, not by rewriting drawing code.
- Liskov Substitution Principle: only matters if you add class inheritance. Avoid inheritance unless it clearly helps.
- Interface Segregation Principle: keep functions small so callers do not depend on behavior they do not need.
- Dependency Inversion Principle: calculation logic should not depend on the UI. The UI should call calculation functions.

Practical rule: keep music theory, app state, and drawing code separated.

### DRY

DRY means "Don't Repeat Yourself."

- Put repeated chord formulas in one data structure.
- Put repeated drawing values, such as colors and marker sizes, in named constants.
- Avoid copying similar blocks for Drop 2, Drop 3, CAGED, and future voicings if a shared helper can handle them.

Do not overdo DRY. If two pieces of code only look similar but mean different things musically, clarity is more important than merging them.

### Avoid Magic Numbers

Magic numbers are hard-coded numeric values whose purpose is unclear from context.

- Use named constants for UI dimensions, spacing, colors, font sizes, line widths, and algorithm thresholds.
- Keep domain data, such as chord intervals and string tuning offsets, in clear data structures.
- Do not replace obvious loop counters or conventional zero-based indexes unless a name improves readability.
- Put drawing-related constants in `src/guitar_chords_viewer/fretboard.py`.
- Put music-theory constants in `src/guitar_chords_viewer/music_theory.py`.
- Put window and control-layout constants in `src/guitar_chords_viewer/ui_tkinter.py`.

Practical rule: a future editor should know what a number controls without tracing the whole program.

### KISS

KISS means "Keep It Simple."

- Prefer plain functions and dictionaries for the music model.
- Avoid frameworks for this app unless the app grows beyond a simple desktop tool.
- Keep app startup simple through the root launcher documented in `SETUP_CHECKLIST.md`.

### Separation Of Concerns

Keep different responsibilities in different sections or files.

- Music data: notes, tunings, chord formulas, and base shapes.
- Music logic: functions that calculate fret positions.
- UI state: selected root, chord quality, voicing shape, inversion, and play mode.
- Drawing logic: code that renders the fretboard and note markers.

This makes the app easier to change without breaking unrelated behavior.

### Testable Core

The calculation logic should be usable without opening a GUI.

Good target:

```python
frets, labels = calculate_fret_positions("Drop 2", "Root Position", "Major 7 (R-3-5-7)", "C")
```

That function should stay independent from `tkinter`.

### Separate Theory From Playability

Chord formulas describe musical identity. Playability rules describe whether a generated grip is practical on guitar.

- Keep interval definitions in `src/guitar_chords_viewer/music_theory.py`.
- Keep physical grip rules in `src/guitar_chords_viewer/playability.py`.
- Let the UI display a computed assessment instead of hard-coding playability text.
- Treat full extended chords as shell voicings when more than four notes would be required.
- Treat CAGED as standard movable chord-shape templates, not as four-note drop voicings.

## Recommended Architecture

The app uses a small layered package:

- launcher
- app entry point
- music theory logic
- playability rules
- fretboard drawing helpers
- tkinter UI
- tests

For the exact folder layout and file responsibilities, see `PROJECT_STRUCTURE.md`.

## Suggested Update Workflow

When you make your own changes:

1. Identify the type of change.
2. Edit the smallest responsible section or file.
3. Run the checks listed in `SETUP_CHECKLIST.md`.
4. Test the UI selection that changed.

## Common Change Examples

### Add A New Chord Quality

Edit `CHORD_QUALITIES`.

Example:

```python
"Minor 6 (R-b3-5-6)": ChordQuality(
    intervals={"R": 0, "3": 3, "5": 7, "7": 9},
    display_labels={"R": "R", "3": "b3", "5": "5", "7": "6"},
    voicing_note="Uses the current seventh-chord slot as a sixth.",
)
```

Note: the current shape data uses four voice slots: `R`, `3`, `5`, and `7`. For shell voicings, map those slots to the four chord tones you want to display.

### Add A New Drop Shape

Edit `BASE_SHAPES`.

Add a new top-level shape name with inversion mappings that follow the existing format:

```python
"Drop 4": {
    "Root Position": {6: (0, "R"), 4: (0, "5"), 3: (1, "7"), 2: (0, "3")},
}
```

### Add A New CAGED Shape

Edit `CAGED_SHAPES`.

Add a new template with its open-position root and string layout:

```python
"CAGED E Shape": {
    "root_note": "E",
    "layout": {6: (0, "R"), 5: (2, "5"), 4: (2, "R"), 3: (1, "3"), 2: (0, "5"), 1: (0, "R")},
}
```

CAGED chord quality options are maintained separately from drop chord qualities because each CAGED chord type owns shape-specific string layouts.

### Change Visual Style

Edit drawing constants or the `draw_fretboard()` method.

Good visual changes:

- note marker colors
- canvas background
- fret line color
- marker size
- window size

Avoid changing music calculation code for visual-only updates.

## Current Best Next Refactor

The package split is complete. The best next refactor is to add a small model object for the selected voicing, so `calculate_fret_positions()` can return named data instead of parallel dictionaries.

That would make tests clearer as chord and voicing features grow.
