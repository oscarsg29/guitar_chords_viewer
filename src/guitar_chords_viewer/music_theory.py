"""Music data and fret-position calculation for guitar chord voicings."""

from dataclasses import dataclass

from guitar_chords_viewer.playability import assess_playability

SEMITONES_PER_OCTAVE = 12
LOW_FRET_WRAP_LIMIT = 2
UPPER_SHAPE_OFFSET_THRESHOLD = 5
HIGH_POSITION_OFFSET_THRESHOLD = 7
HIGH_POSITION_WRAP_LIMIT = 5

CHROMATIC_SCALE = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
STRING_TUNING_OFFSETS = {1: 4, 2: 11, 3: 7, 4: 2, 5: 9, 6: 4}
STRING_NAMES = {1: "E", 2: "B", 3: "G", 4: "D", 5: "A", 6: "E"}


@dataclass(frozen=True)
class ChordQuality:
    """Four-note chord quality that can use the current drop-voicing shapes."""

    intervals: dict[str, int]
    display_labels: dict[str, str]
    voicing_note: str


CHORD_QUALITIES = {
    "Major 7 (R-3-5-7)": ChordQuality(
        intervals={"R": 0, "3": 4, "5": 7, "7": 11},
        display_labels={"R": "R", "3": "3", "5": "5", "7": "7"},
        voicing_note="Standard four-note Drop 2/Drop 3 seventh-chord voicing.",
    ),
    "Minor 7 (R-b3-5-b7)": ChordQuality(
        intervals={"R": 0, "3": 3, "5": 7, "7": 10},
        display_labels={"R": "R", "3": "b3", "5": "5", "7": "b7"},
        voicing_note="Standard four-note Drop 2/Drop 3 minor seventh voicing.",
    ),
    "Dominant 7 (R-3-5-b7)": ChordQuality(
        intervals={"R": 0, "3": 4, "5": 7, "7": 10},
        display_labels={"R": "R", "3": "3", "5": "5", "7": "b7"},
        voicing_note="Standard four-note Drop 2/Drop 3 dominant seventh voicing.",
    ),
    "Major 6 (R-3-5-6)": ChordQuality(
        intervals={"R": 0, "3": 4, "5": 7, "7": 9},
        display_labels={"R": "R", "3": "3", "5": "5", "7": "6"},
        voicing_note="Uses the current seventh-chord slot as a sixth.",
    ),
    "Minor 6 (R-b3-5-6)": ChordQuality(
        intervals={"R": 0, "3": 3, "5": 7, "7": 9},
        display_labels={"R": "R", "3": "b3", "5": "5", "7": "6"},
        voicing_note="Uses the current seventh-chord slot as a sixth.",
    ),
    "Minor 7 b5 (R-b3-b5-b7)": ChordQuality(
        intervals={"R": 0, "3": 3, "5": 6, "7": 10},
        display_labels={"R": "R", "3": "b3", "5": "b5", "7": "b7"},
        voicing_note="Common four-note half-diminished guitar voicing.",
    ),
    "Diminished 7 (R-b3-b5-bb7)": ChordQuality(
        intervals={"R": 0, "3": 3, "5": 6, "7": 9},
        display_labels={"R": "R", "3": "b3", "5": "b5", "7": "bb7"},
        voicing_note="Compact symmetrical four-note diminished seventh voicing.",
    ),
    "Minor Major 7 (R-b3-5-7)": ChordQuality(
        intervals={"R": 0, "3": 3, "5": 7, "7": 11},
        display_labels={"R": "R", "3": "b3", "5": "5", "7": "7"},
        voicing_note="Four-note voicing, but some grips may feel less common.",
    ),
    "Augmented Major 7 (R-3-#5-7)": ChordQuality(
        intervals={"R": 0, "3": 4, "5": 8, "7": 11},
        display_labels={"R": "R", "3": "3", "5": "#5", "7": "7"},
        voicing_note="Four-note augmented major seventh voicing.",
    ),
    "Augmented Dominant 7 (R-3-#5-b7)": ChordQuality(
        intervals={"R": 0, "3": 4, "5": 8, "7": 10},
        display_labels={"R": "R", "3": "3", "5": "#5", "7": "b7"},
        voicing_note="Four-note augmented dominant voicing.",
    ),
    "Dominant 7 b5 (R-3-b5-b7)": ChordQuality(
        intervals={"R": 0, "3": 4, "5": 6, "7": 10},
        display_labels={"R": "R", "3": "3", "5": "b5", "7": "b7"},
        voicing_note="Common four-note altered dominant voicing.",
    ),
    "Dominant 7 #5 (R-3-#5-b7)": ChordQuality(
        intervals={"R": 0, "3": 4, "5": 8, "7": 10},
        display_labels={"R": "R", "3": "3", "5": "#5", "7": "b7"},
        voicing_note="Common four-note altered dominant voicing.",
    ),
    "Dominant 7 sus4 (R-4-5-b7)": ChordQuality(
        intervals={"R": 0, "3": 5, "5": 7, "7": 10},
        display_labels={"R": "R", "3": "4", "5": "5", "7": "b7"},
        voicing_note="Four-note suspended dominant voicing.",
    ),
    "Major 7 #11 shell (R-3-7-#11)": ChordQuality(
        intervals={"R": 0, "3": 4, "5": 11, "7": 6},
        display_labels={"R": "R", "3": "3", "5": "7", "7": "#11"},
        voicing_note="Shell voicing: omits the fifth to fit a four-note guitar grip.",
    ),
    "Dominant 9 shell (R-3-b7-9)": ChordQuality(
        intervals={"R": 0, "3": 4, "5": 10, "7": 14},
        display_labels={"R": "R", "3": "3", "5": "b7", "7": "9"},
        voicing_note="Shell voicing: omits the fifth to fit a four-note guitar grip.",
    ),
    "Minor 9 shell (R-b3-b7-9)": ChordQuality(
        intervals={"R": 0, "3": 3, "5": 10, "7": 14},
        display_labels={"R": "R", "3": "b3", "5": "b7", "7": "9"},
        voicing_note="Shell voicing: omits the fifth to fit a four-note guitar grip.",
    ),
    "Major 9 shell (R-3-7-9)": ChordQuality(
        intervals={"R": 0, "3": 4, "5": 11, "7": 14},
        display_labels={"R": "R", "3": "3", "5": "7", "7": "9"},
        voicing_note="Shell voicing: omits the fifth to fit a four-note guitar grip.",
    ),
    "6/9 shell (R-3-6-9)": ChordQuality(
        intervals={"R": 0, "3": 4, "5": 9, "7": 14},
        display_labels={"R": "R", "3": "3", "5": "6", "7": "9"},
        voicing_note="Shell voicing: four-note sixth/ninth guitar voicing.",
    ),
    "Minor 6/9 shell (R-b3-6-9)": ChordQuality(
        intervals={"R": 0, "3": 3, "5": 9, "7": 14},
        display_labels={"R": "R", "3": "b3", "5": "6", "7": "9"},
        voicing_note="Shell voicing: four-note minor sixth/ninth guitar voicing.",
    ),
    "9sus4 shell (R-4-b7-9)": ChordQuality(
        intervals={"R": 0, "3": 5, "5": 10, "7": 14},
        display_labels={"R": "R", "3": "4", "5": "b7", "7": "9"},
        voicing_note="Shell voicing: suspended dominant sound with the fifth omitted.",
    ),
    "13 shell (R-3-b7-13)": ChordQuality(
        intervals={"R": 0, "3": 4, "5": 10, "7": 21},
        display_labels={"R": "R", "3": "3", "5": "b7", "7": "13"},
        voicing_note="Shell voicing: omits the fifth and ninth/eleventh color tones.",
    ),
    "Minor 11 shell (R-b3-b7-11)": ChordQuality(
        intervals={"R": 0, "3": 3, "5": 10, "7": 17},
        display_labels={"R": "R", "3": "b3", "5": "b7", "7": "11"},
        voicing_note="Shell voicing: omits the fifth and ninth to fit a four-note guitar grip.",
    ),
}

BASE_SHAPES = {
    "Drop 2": {
        "Root Position": {4: (0, "R"), 3: (0, "5"), 2: (1, "7"), 1: (0, "3")},
        "1st Inversion": {4: (4, "3"), 3: (3, "7"), 2: (3, "R"), 1: (3, "5")},
        "2nd Inversion": {4: (7, "5"), 3: (7, "R"), 2: (8, "3"), 1: (7, "7")},
        "3rd Inversion": {4: (11, "7"), 3: (11, "3"), 2: (10, "5"), 1: (10, "R")},
    },
    "Drop 3": {
        "Root Position": {5: (0, "R"), 3: (1, "7"), 2: (1, "3"), 1: (0, "5")},
        "1st Inversion": {5: (4, "3"), 3: (3, "R"), 2: (3, "5"), 1: (4, "7")},
        "2nd Inversion": {5: (7, "5"), 3: (8, "3"), 2: (7, "7"), 1: (7, "R")},
        "3rd Inversion": {5: (11, "7"), 3: (10, "5"), 2: (10, "R"), 1: (11, "3")},
    },
}


def get_root_notes():
    """Return the supported root notes."""
    return list(CHROMATIC_SCALE)


def get_chord_families():
    """Return the supported chord quality names."""
    return list(CHORD_QUALITIES)


def get_chord_types():
    """Return the supported drop voicing type names."""
    return list(BASE_SHAPES)


def get_inversions(chord_type):
    """Return inversion names for a drop voicing type."""
    return list(BASE_SHAPES[chord_type])


def get_voicing_note(chord_family):
    """Return the static voicing note for a supported chord quality."""
    return CHORD_QUALITIES[chord_family].voicing_note


def assess_chord_playability(chord_type, inversion, chord_family, root_note):
    """Return the physical playability assessment for a selected voicing."""
    frets, _labels = calculate_fret_positions(chord_type, inversion, chord_family, root_note)
    return assess_playability(frets, CHORD_QUALITIES[chord_family].voicing_note)


def calculate_fret_positions(chord_type, inversion, chord_family, root_note):
    """Calculate playable fret positions for a selected drop chord voicing."""
    root_index = CHROMATIC_SCALE.index(root_note)
    base_layout = BASE_SHAPES[chord_type][inversion]
    chord_quality = CHORD_QUALITIES[chord_family]

    final_frets = {}
    final_labels = {}

    for string, (base_fret_offset, interval_type) in base_layout.items():
        interval_modifier = chord_quality.intervals[interval_type]
        target_pitch = (root_index + interval_modifier) % SEMITONES_PER_OCTAVE
        string_open_pitch = STRING_TUNING_OFFSETS[string]

        fret = (target_pitch - string_open_pitch) % SEMITONES_PER_OCTAVE
        if fret < LOW_FRET_WRAP_LIMIT and base_fret_offset > UPPER_SHAPE_OFFSET_THRESHOLD:
            fret += SEMITONES_PER_OCTAVE
        elif base_fret_offset >= HIGH_POSITION_OFFSET_THRESHOLD and fret < HIGH_POSITION_WRAP_LIMIT:
            fret += SEMITONES_PER_OCTAVE

        final_frets[string] = fret
        final_labels[string] = chord_quality.display_labels[interval_type]

    return final_frets, final_labels
