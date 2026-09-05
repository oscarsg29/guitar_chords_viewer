"""Music data and fret-position calculation for guitar chord voicings."""

SEMITONES_PER_OCTAVE = 12
LOW_FRET_WRAP_LIMIT = 2
UPPER_SHAPE_OFFSET_THRESHOLD = 5
HIGH_POSITION_OFFSET_THRESHOLD = 7
HIGH_POSITION_WRAP_LIMIT = 5

CHROMATIC_SCALE = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
STRING_TUNING_OFFSETS = {1: 4, 2: 11, 3: 7, 4: 2, 5: 9, 6: 4}
STRING_NAMES = {1: "E", 2: "B", 3: "G", 4: "D", 5: "A", 6: "E"}

CHORD_FORMULAS = {
    "Major 7 (R-3-5-7)": {"R": 0, "3": 4, "5": 7, "7": 11},
    "Minor 7 (R-b3-5-b7)": {"R": 0, "3": 3, "5": 7, "7": 10},
    "Dominant 7 (R-3-5-b7)": {"R": 0, "3": 4, "5": 7, "7": 10},
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
    return list(CHORD_FORMULAS)


def get_chord_types():
    """Return the supported drop voicing type names."""
    return list(BASE_SHAPES)


def get_inversions(chord_type):
    """Return inversion names for a drop voicing type."""
    return list(BASE_SHAPES[chord_type])


def calculate_fret_positions(chord_type, inversion, chord_family, root_note):
    """Calculate playable fret positions for a selected drop chord voicing."""
    root_index = CHROMATIC_SCALE.index(root_note)
    base_layout = BASE_SHAPES[chord_type][inversion]
    formula = CHORD_FORMULAS[chord_family]

    final_frets = {}
    final_labels = {}

    for string, (base_fret_offset, interval_type) in base_layout.items():
        interval_modifier = formula[interval_type[0]]
        target_pitch = (root_index + interval_modifier) % SEMITONES_PER_OCTAVE
        string_open_pitch = STRING_TUNING_OFFSETS[string]

        fret = (target_pitch - string_open_pitch) % SEMITONES_PER_OCTAVE
        if fret < LOW_FRET_WRAP_LIMIT and base_fret_offset > UPPER_SHAPE_OFFSET_THRESHOLD:
            fret += SEMITONES_PER_OCTAVE
        elif base_fret_offset >= HIGH_POSITION_OFFSET_THRESHOLD and fret < HIGH_POSITION_WRAP_LIMIT:
            fret += SEMITONES_PER_OCTAVE

        final_frets[string] = fret
        final_labels[string] = interval_type

    return final_frets, final_labels
