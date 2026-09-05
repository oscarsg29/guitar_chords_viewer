# Script Features And Intention

`guitarChordsViewer.py` is intended to be an interactive native Python desktop app for visualizing guitar drop chord voicings.

## Main Intention

The script helps a guitarist explore seventh-chord voicings across:

- Root notes
- Chord qualities
- Drop voicing types
- Inversions

It calculates fret positions and displays the selected voicing as a local desktop fretboard-style diagram.

## Current Features

- Defines a chromatic note map from `C` through `B`.
- Defines standard guitar tuning offsets for six strings.
- Supports these chord qualities:
  - Major 7
  - Minor 7
  - Dominant 7
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
- Highlights root notes in green and other chord tones in blue.
- Displays a status line summarizing the selected chord and voicing.

## Implementation Notes

- The music calculation is centered around `calculate_fret_positions()`.
- Non-obvious numeric values are named as constants in the module that owns the related behavior.
- The detailed folder layout and file responsibilities are documented in `PROJECT_STRUCTURE.md`.
- Run and verification commands are documented in `SETUP_CHECKLIST.md`.

## Possible Improvements

- Add tests for `calculate_fret_positions()`.
- Split app rendering from music calculation logic to make the calculation easier to test.
- Add more chord qualities, tunings, and voicing families.
- Add a save/export image command.
