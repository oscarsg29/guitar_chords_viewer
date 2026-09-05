# Script Features And Intention

`guitarChordsViewer.py` is intended to be an interactive native Python desktop app for visualizing guitar-playable drop chord voicings.

## Main Intention

The script helps a guitarist explore four-note voicings across:

- Root notes
- Chord qualities
- Drop voicing types
- Inversions

It calculates fret positions and displays the selected voicing as a local desktop fretboard-style diagram.

## Current Features

- Defines a chromatic note map from `C` through `B`.
- Defines standard guitar tuning offsets for six strings.
- Supports these guitar-playable four-note chord qualities:
  - Major 7
  - Minor 7
  - Dominant 7
  - Major 6
  - Minor 6
  - Minor 7 b5
  - Diminished 7
  - Minor Major 7
  - Augmented Major 7
  - Augmented Dominant 7
  - Dominant 7 b5
  - Dominant 7 #5
  - Dominant 7 sus4
  - Major 7 #11 shell
  - Dominant 9 shell
  - Minor 9 shell
  - Major 9 shell
  - 6/9 shell
  - Minor 6/9 shell
  - 9sus4 shell
  - 13 shell
  - Minor 11 shell
- Supports these voicing families:
  - Drop 2
  - Drop 3
- Supports these inversion structures:
  - Root Position
  - 1st Inversion
  - 2nd Inversion
  - 3rd Inversion
- Provides native desktop dropdown controls for choosing:
  - Key root
  - Chord quality
  - Drop type
  - Inversion
- Calculates fret positions dynamically based on the selected root and chord formula.
- Uses a `tkinter.Canvas` to draw:
  - Vertical fret markers
  - Horizontal string lines
  - Note markers with interval labels
- Places note markers in the fret space behind the fret line instead of directly on top of the fret.
- Highlights root notes in green and other chord tones in blue.
- Displays a status line summarizing the selected chord and voicing.
- Displays a computed playability assessment for the selected grip.

## Implementation Notes

- The music calculation is centered around `calculate_fret_positions()`.
- Physical guitar playability is assessed by `src/guitar_chords_viewer/playability.py`.
- Non-obvious numeric values are named as constants in the module that owns the related behavior.
- The detailed folder layout and file responsibilities are documented in `PROJECT_STRUCTURE.md`.
- Run and verification commands are documented in `SETUP_CHECKLIST.md`.

## Possible Improvements

- Add curated triad shapes for three-note voicings.
- Add finger-aware playability checks, including barre and finger-collision rules.
- Add more tunings and voicing families.
- Add a save/export image command.
