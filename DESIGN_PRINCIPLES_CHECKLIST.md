# Design Principles Checklist

This checklist rates how well the app currently follows the design principles in `DESIGN_PRINCIPLES.md`.

Rating scale:

- 1 = weak
- 2 = partial
- 3 = good
- 4 = strong
- 5 = excellent

## Current Score

- [x] Single Responsibility Principle: 4/5
  - Music logic, fretboard drawing helpers, UI code, and app entry point are split into separate package modules.
  - The UI class still owns several UI drawing methods, which is acceptable for this app size.
- [x] Open/Closed Principle: 4/5
  - New chord qualities, drop shapes, and CAGED templates can mostly be added by editing data in `src/guitar_chords_viewer/music_theory.py`.
  - Drop chord qualities and CAGED chord types carry their own display labels and voicing notes.
  - Larger full extended chords still need curated guitar voicing rules if they require more than four notes.
- [x] Liskov Substitution Principle: 5/5
  - The app does not use inheritance except `tk.Tk`, so there is no custom inheritance hierarchy to violate.
- [x] Interface Segregation Principle: 5/5
  - Small getter functions expose UI option lists.
  - `calculate_voicing()` exposes named result data while `calculate_fret_positions()` remains a compatibility wrapper.
  - Drawing helpers are focused and do not force callers to depend on the full UI.
- [x] Dependency Inversion Principle: 5/5
  - UI code depends on pure music functions.
  - Music logic does not depend on `tkinter`.
  - Architecture tests guard domain modules against UI and app-layer imports.
- [x] Theory vs Playability Separation: 4/5
  - Chord definitions and physical grip assessment are separated.
  - Playability is computed from generated fret positions instead of hard-coded in the UI.
  - The current rules are intentionally simple and do not yet model fingers or barre mechanics.
- [x] DRY: 4/5
  - Shared constants are centralized in `src/guitar_chords_viewer/music_theory.py` and `src/guitar_chords_viewer/fretboard.py`.
  - Some canvas drawing code is still naturally explicit for readability.
- [x] Avoid Magic Numbers: 4/5
  - Music-theory thresholds and octave math are named in `src/guitar_chords_viewer/music_theory.py`.
  - Fretboard layout, drawing widths, offsets, marker sizing, and fonts are named in `src/guitar_chords_viewer/fretboard.py`.
  - Window sizing, padding, and control-layout values are named in `src/guitar_chords_viewer/ui_tkinter.py`.
  - Remaining numeric values in chord formulas, tuning offsets, and base shapes are intentional domain data.
- [x] KISS: 5/5
  - The app uses only Python standard library modules.
  - The launcher remains simple and is documented in `SETUP_CHECKLIST.md`.
- [x] Separation of Concerns: 5/5
  - Music data, drawing helpers, audio, UI, app entry, and launcher responsibilities are split.
  - Exact file ownership is documented in `PROJECT_STRUCTURE.md`.
- [x] Audio Separation: 4/5
  - Audio synthesis and playback live in `src/guitar_chords_viewer/audio.py`.
  - The UI only passes the selected frets and play mode into the audio layer.
  - The current synth is procedural and dependency-free, so realistic instrument quality is intentionally limited.
- [x] Testable Core: 5/5
  - `calculate_voicing()` can be tested without opening the GUI.
  - Unit tests cover supported chord-family options, altered labels, shell labels, CAGED transposition, voicing notes, UI geometry helpers, playability assessments, architecture boundaries, and shape-data validation.

## Overall Rating

Current architecture score: 5/5.

The app now follows the recommended principles well for a small desktop tool. The most useful next improvement is adding finger-aware playability checks for barre and partial-barre shapes.

## Maintenance Checklist

Use this before making changes:

- [ ] Am I changing music data? Edit `src/guitar_chords_viewer/music_theory.py`.
- [ ] Am I changing fretboard colors, spacing, or marker sizes? Edit `src/guitar_chords_viewer/fretboard.py`.
- [ ] Am I changing dropdowns, events, or window behavior? Edit `src/guitar_chords_viewer/ui_tkinter.py`.
- [ ] Am I changing how the app starts? Edit `src/guitar_chords_viewer/app.py` or `guitarChordsViewer.py`.
- [ ] Did I check `PROJECT_STRUCTURE.md` if I was unsure where a change belongs?
- [ ] Did I avoid duplicating chord formulas or shape data?
- [ ] Did I name non-obvious numeric values instead of adding magic numbers?
- [ ] Did I keep music calculation independent from `tkinter`?
- [ ] Did I keep chord theory separate from physical playability rules?
- [ ] Did I run syntax checks?
- [ ] Did I run tests?
- [ ] Did I launch the app and verify the changed UI path?

## Verification Commands

Use the verification commands in `SETUP_CHECKLIST.md`.
