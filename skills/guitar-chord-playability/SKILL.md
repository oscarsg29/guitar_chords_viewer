---
name: guitar-chord-playability
description: Assess whether generated guitar chord voicings are playable, stretchy, or not recommended based on practical fretting rules.
metadata:
  short-description: Assess guitar chord playability
---

# Guitar Chord Playability

Use this skill when adding, reviewing, or changing guitar chord voicings. The goal is to distinguish theoretical chord formulas from practical guitar grips.

## Core Rules

A voicing is supported by the current simple app model when:

- Drop voicings use no more than four notes.
- Drop voicings map to the app's four voice slots.
- CAGED shapes may use up to six sounded strings when they follow standard movable CAGED templates.
- It uses a supported string set, such as Drop 2, Drop 3, or one of the CAGED standard shapes.
- Extended chords are reduced to shell voicings when a full chord would require more than four notes.

## Physical Playability Ratings

Use fret span as the first practical check. Ignore open strings when calculating fret span.

- `playable`: fretted notes fit within a small span.
- `stretchy`: fretted notes are possible but may feel uncomfortable.
- `not recommended`: the fret span is too wide, the grip uses too many sounded strings for the selected model, or the position is unusually high.

For this app's rule implementation:

- `playable`: fret span is 3 frets or less.
- `stretchy`: fret span is 4 or 5 frets.
- `not recommended`: fret span is more than 5 frets.
- `not recommended`: highest fret is above fret 18.
- Open strings do not count against fret span.
- Drop voicings are limited to four sounded strings.
- CAGED standard shapes can use up to six sounded strings because duplicate chord tones are part of many shapes.

## Shell Voicing Rules

For 9th, 11th, and 13th chords, prefer curated shell voicings over full formulas.

Common omissions:

- Dominant 9: use `R-3-b7-9`, omit `5`.
- Major 9: use `R-3-7-9`, omit `5`.
- Minor 9: use `R-b3-b7-9`, omit `5`.
- Major 7 #11: use `R-3-7-#11`, omit `5`.
- 13 shell: use `R-3-b7-13`, omit `5`, `9`, and `11`.
- Minor 11 shell: use `R-b3-b7-11`, omit `5` and `9`.

## Implementation Guidance

Keep chord identity and physical playability separate:

- Chord definitions describe intervals, display labels, and voicing intent.
- Playability rules inspect generated fret positions.
- UI should display the computed playability assessment, not hard-code the result.

When changing rules, update tests that cover:

- easy/playable grips
- stretchy grips
- not recommended grips
- open-string handling
- shell voicing labels
