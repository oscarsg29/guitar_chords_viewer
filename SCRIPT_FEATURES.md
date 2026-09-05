# Script Features And Intention

`guitarChordsViewer.py` is intended to be an interactive native Python desktop app for visualizing guitar-playable drop voicings and CAGED chord shapes.

## Main Intention

The script helps a guitarist explore four-note drop voicings and standard CAGED shapes across:

- Root notes
- Chord qualities
- Voicing shapes
- CAGED standard shapes
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
  - CAGED C Shape
  - CAGED A Shape
  - CAGED G Shape
  - CAGED E Shape
  - CAGED D Shape
- Supports these CAGED chord types:
  - Major triad
  - Minor triad
  - Dominant 7
  - Major 7
  - Minor 7
  - Major 6
  - Minor 6
  - Suspended 2
  - Suspended 4
  - Add 9
  - Diminished triad
  - Augmented triad
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
- Opens centered on the screen and stays above other windows without becoming modal.
- Provides a Play button for hearing the selected chord.
- Provides these play modes:
  - Chord
  - Arpeggio
- Calculates fret positions dynamically based on the selected root and chord formula.
- Uses a `tkinter.Canvas` to draw:
  - Vertical fret markers
  - Horizontal string lines
  - Note markers with interval labels
- Places note markers in the fret space behind the fret line instead of directly on top of the fret.
- Highlights root notes in green and other chord tones in blue.
- Displays a status line summarizing the selected chord and voicing.
- Displays a computed playability assessment for the selected grip.
- Synthesizes cleaner electric-guitar style audio locally as a temporary WAV file.

## Implementation Notes

- The music calculation is centered around `calculate_voicing()`, with `calculate_fret_positions()` kept as a compatibility wrapper.
- Physical guitar playability is assessed by `src/guitar_chords_viewer/playability.py`.
- Audio generation and playback are handled by `src/guitar_chords_viewer/audio.py`.
- Non-obvious numeric values are named as constants in the module that owns the related behavior.
- The detailed folder layout and file responsibilities are documented in `PROJECT_STRUCTURE.md`.
- Run and verification commands are documented in `SETUP_CHECKLIST.md`.

## Possible Improvements

- Add curated triad shapes for three-note voicings.
- Add finger-aware playability checks, including barre and finger-collision rules.
- Add configurable audio controls such as duration, tone, or playback volume.
- Add more tunings and voicing families.
- Add a save/export image command.
