"""Music data and fret-position calculation for guitar chord voicings."""

from dataclasses import dataclass

from guitar_chords_viewer.playability import MAX_NOTES_IN_CAGED_MODEL, assess_playability

SEMITONES_PER_OCTAVE = 12
LOW_FRET_WRAP_LIMIT = 2
UPPER_SHAPE_OFFSET_THRESHOLD = 5
HIGH_POSITION_OFFSET_THRESHOLD = 7
HIGH_POSITION_WRAP_LIMIT = 5
CAGED_FRET_SEARCH_OCTAVES = 3

CHROMATIC_SCALE = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
STRING_TUNING_OFFSETS = {1: 4, 2: 11, 3: 7, 4: 2, 5: 9, 6: 4}
STRING_NAMES = {1: "E", 2: "B", 3: "G", 4: "D", 5: "A", 6: "E"}
CAGED_INVERSION = "Standard Shape"
CAGED_MAJOR = "Major triad (R-3-5)"
CAGED_MINOR = "Minor triad (R-b3-5)"
CAGED_DOMINANT_7 = "Dominant 7 (R-3-5-b7)"
CAGED_MAJOR_7 = "Major 7 (R-3-5-7)"
CAGED_MINOR_7 = "Minor 7 (R-b3-5-b7)"
CAGED_MAJOR_6 = "Major 6 (R-3-5-6)"
CAGED_MINOR_6 = "Minor 6 (R-b3-5-6)"
CAGED_SUS2 = "Suspended 2 (R-2-5)"
CAGED_SUS4 = "Suspended 4 (R-4-5)"
CAGED_ADD9 = "Add 9 (R-3-5-9)"
CAGED_DIMINISHED = "Diminished triad (R-b3-b5)"
CAGED_AUGMENTED = "Augmented triad (R-3-#5)"


@dataclass(frozen=True)
class ChordQuality:
    """Four-note chord quality that can use the current drop-voicing shapes."""

    intervals: dict[str, int]
    display_labels: dict[str, str]
    voicing_note: str


@dataclass(frozen=True)
class FretPosition:
    """A sounded note on one guitar string."""

    string: int
    fret: int
    label: str


@dataclass(frozen=True)
class VoicingResult:
    """Calculated fretboard result for one selected voicing."""

    chord_type: str
    inversion: str
    chord_family: str
    root_note: str
    positions: tuple[FretPosition, ...]
    voicing_note: str
    max_note_count: int | None = None

    @property
    def frets(self):
        """Return fret positions keyed by string for legacy callers."""
        return {position.string: position.fret for position in self.positions}

    @property
    def labels(self):
        """Return displayed note labels keyed by string for legacy callers."""
        return {position.string: position.label for position in self.positions}


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

CAGED_CHORD_QUALITIES = {
    CAGED_MAJOR: ChordQuality(
        intervals={"R": 0, "3": 4, "5": 7},
        display_labels={"R": "R", "3": "3", "5": "5"},
        voicing_note="Standard movable CAGED major-triad shape.",
    ),
    CAGED_MINOR: ChordQuality(
        intervals={"R": 0, "b3": 3, "5": 7},
        display_labels={"R": "R", "b3": "b3", "5": "5"},
        voicing_note="Minor-triad variation based on the movable CAGED shape.",
    ),
    CAGED_DOMINANT_7: ChordQuality(
        intervals={"R": 0, "3": 4, "5": 7, "b7": 10},
        display_labels={"R": "R", "3": "3", "5": "5", "b7": "b7"},
        voicing_note="Movable CAGED dominant seventh shape.",
    ),
    CAGED_MAJOR_7: ChordQuality(
        intervals={"R": 0, "3": 4, "5": 7, "7": 11},
        display_labels={"R": "R", "3": "3", "5": "5", "7": "7"},
        voicing_note="Movable CAGED major seventh shape.",
    ),
    CAGED_MINOR_7: ChordQuality(
        intervals={"R": 0, "b3": 3, "5": 7, "b7": 10},
        display_labels={"R": "R", "b3": "b3", "5": "5", "b7": "b7"},
        voicing_note="Movable CAGED minor seventh shape.",
    ),
    CAGED_MAJOR_6: ChordQuality(
        intervals={"R": 0, "3": 4, "5": 7, "6": 9},
        display_labels={"R": "R", "3": "3", "5": "5", "6": "6"},
        voicing_note="Movable CAGED sixth-chord shape.",
    ),
    CAGED_MINOR_6: ChordQuality(
        intervals={"R": 0, "b3": 3, "5": 7, "6": 9},
        display_labels={"R": "R", "b3": "b3", "5": "5", "6": "6"},
        voicing_note="Movable CAGED minor sixth-chord shape.",
    ),
    CAGED_SUS2: ChordQuality(
        intervals={"R": 0, "2": 2, "5": 7},
        display_labels={"R": "R", "2": "2", "5": "5"},
        voicing_note="Movable CAGED suspended second shape.",
    ),
    CAGED_SUS4: ChordQuality(
        intervals={"R": 0, "4": 5, "5": 7},
        display_labels={"R": "R", "4": "4", "5": "5"},
        voicing_note="Movable CAGED suspended fourth shape.",
    ),
    CAGED_ADD9: ChordQuality(
        intervals={"R": 0, "3": 4, "5": 7, "9": 14},
        display_labels={"R": "R", "3": "3", "5": "5", "9": "9"},
        voicing_note="Movable CAGED add9 shape.",
    ),
    CAGED_DIMINISHED: ChordQuality(
        intervals={"R": 0, "b3": 3, "b5": 6},
        display_labels={"R": "R", "b3": "b3", "b5": "b5"},
        voicing_note="Movable CAGED diminished-triad shape.",
    ),
    CAGED_AUGMENTED: ChordQuality(
        intervals={"R": 0, "3": 4, "#5": 8},
        display_labels={"R": "R", "3": "3", "#5": "#5"},
        voicing_note="Movable CAGED augmented-triad shape.",
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

CAGED_SHAPES = {
    "CAGED C Shape": {
        "root_note": "C",
        "layouts": {
            CAGED_MAJOR: {5: (3, "R"), 4: (2, "3"), 3: (0, "5"), 2: (1, "R"), 1: (0, "3")},
            CAGED_MINOR: {5: (3, "R"), 4: (1, "b3"), 3: (0, "5"), 2: (1, "R"), 1: (3, "5")},
            CAGED_DOMINANT_7: {5: (3, "R"), 4: (2, "3"), 3: (3, "b7"), 2: (1, "R"), 1: (0, "3")},
            CAGED_MAJOR_7: {5: (3, "R"), 4: (2, "3"), 3: (0, "5"), 2: (0, "7"), 1: (0, "3")},
            CAGED_MINOR_7: {5: (3, "R"), 4: (1, "b3"), 3: (3, "b7"), 2: (1, "R"), 1: (3, "5")},
            CAGED_MAJOR_6: {5: (3, "R"), 4: (2, "3"), 3: (2, "6"), 2: (1, "R"), 1: (0, "3")},
            CAGED_MINOR_6: {5: (3, "R"), 4: (1, "b3"), 3: (2, "6"), 2: (1, "R"), 1: (3, "5")},
            CAGED_SUS2: {5: (3, "R"), 4: (0, "2"), 3: (0, "5"), 2: (1, "R"), 1: (3, "5")},
            CAGED_SUS4: {5: (3, "R"), 4: (3, "4"), 3: (0, "5"), 2: (1, "R"), 1: (1, "4")},
            CAGED_ADD9: {5: (3, "R"), 4: (2, "3"), 3: (0, "5"), 2: (3, "9"), 1: (0, "3")},
            CAGED_DIMINISHED: {5: (3, "R"), 4: (1, "b3"), 3: (2, "b5"), 2: (1, "R")},
            CAGED_AUGMENTED: {5: (3, "R"), 4: (2, "3"), 3: (1, "#5"), 2: (1, "R"), 1: (0, "3")},
        },
    },
    "CAGED A Shape": {
        "root_note": "A",
        "layouts": {
            CAGED_MAJOR: {5: (0, "R"), 4: (2, "5"), 3: (2, "R"), 2: (2, "3"), 1: (0, "5")},
            CAGED_MINOR: {5: (0, "R"), 4: (2, "5"), 3: (2, "R"), 2: (1, "b3"), 1: (0, "5")},
            CAGED_DOMINANT_7: {5: (0, "R"), 4: (2, "5"), 3: (0, "b7"), 2: (2, "3"), 1: (0, "5")},
            CAGED_MAJOR_7: {5: (0, "R"), 4: (2, "5"), 3: (1, "7"), 2: (2, "3"), 1: (0, "5")},
            CAGED_MINOR_7: {5: (0, "R"), 4: (2, "5"), 3: (0, "b7"), 2: (1, "b3"), 1: (0, "5")},
            CAGED_MAJOR_6: {5: (0, "R"), 4: (2, "5"), 3: (2, "R"), 2: (2, "3"), 1: (2, "6")},
            CAGED_MINOR_6: {5: (0, "R"), 4: (2, "5"), 3: (2, "R"), 2: (1, "b3"), 1: (2, "6")},
            CAGED_SUS2: {5: (0, "R"), 4: (2, "5"), 3: (2, "R"), 2: (0, "2"), 1: (0, "5")},
            CAGED_SUS4: {5: (0, "R"), 4: (2, "5"), 3: (2, "R"), 2: (3, "4"), 1: (0, "5")},
            CAGED_ADD9: {5: (0, "R"), 4: (2, "5"), 3: (4, "9"), 2: (2, "3"), 1: (0, "5")},
            CAGED_DIMINISHED: {5: (0, "R"), 4: (1, "b5"), 3: (2, "R"), 2: (1, "b3")},
            CAGED_AUGMENTED: {5: (0, "R"), 4: (3, "#5"), 3: (2, "R"), 2: (2, "3"), 1: (1, "#5")},
        },
    },
    "CAGED G Shape": {
        "root_note": "G",
        "layouts": {
            CAGED_MAJOR: {6: (3, "R"), 5: (2, "3"), 4: (0, "5"), 3: (0, "R"), 2: (0, "3"), 1: (3, "R")},
            CAGED_MINOR: {6: (3, "R"), 5: (1, "b3"), 4: (0, "5"), 3: (0, "R"), 2: (3, "b3"), 1: (3, "R")},
            CAGED_DOMINANT_7: {6: (3, "R"), 5: (2, "3"), 4: (0, "5"), 3: (0, "R"), 2: (0, "3"), 1: (1, "b7")},
            CAGED_MAJOR_7: {6: (3, "R"), 5: (2, "3"), 4: (0, "5"), 3: (0, "R"), 2: (0, "3"), 1: (2, "7")},
            CAGED_MINOR_7: {6: (3, "R"), 5: (1, "b3"), 4: (0, "5"), 3: (0, "R"), 2: (3, "b3"), 1: (1, "b7")},
            CAGED_MAJOR_6: {6: (3, "R"), 5: (2, "3"), 4: (0, "5"), 3: (0, "R"), 2: (0, "3"), 1: (0, "6")},
            CAGED_MINOR_6: {6: (3, "R"), 5: (1, "b3"), 4: (0, "5"), 3: (0, "R"), 2: (3, "b3"), 1: (0, "6")},
            CAGED_SUS2: {6: (3, "R"), 5: (0, "2"), 4: (0, "5"), 3: (0, "R"), 2: (3, "2"), 1: (3, "R")},
            CAGED_SUS4: {6: (3, "R"), 5: (3, "4"), 4: (0, "5"), 3: (0, "R"), 2: (1, "4"), 1: (3, "R")},
            CAGED_ADD9: {6: (3, "R"), 5: (2, "3"), 4: (0, "5"), 3: (2, "9"), 2: (0, "3"), 1: (3, "R")},
            CAGED_DIMINISHED: {6: (3, "R"), 5: (1, "b3"), 4: (2, "b5"), 3: (0, "R")},
            CAGED_AUGMENTED: {6: (3, "R"), 5: (2, "3"), 4: (1, "#5"), 3: (0, "R"), 2: (0, "3"), 1: (3, "R")},
        },
    },
    "CAGED E Shape": {
        "root_note": "E",
        "layouts": {
            CAGED_MAJOR: {6: (0, "R"), 5: (2, "5"), 4: (2, "R"), 3: (1, "3"), 2: (0, "5"), 1: (0, "R")},
            CAGED_MINOR: {6: (0, "R"), 5: (2, "5"), 4: (2, "R"), 3: (0, "b3"), 2: (0, "5"), 1: (0, "R")},
            CAGED_DOMINANT_7: {6: (0, "R"), 5: (2, "5"), 4: (0, "b7"), 3: (1, "3"), 2: (0, "5"), 1: (0, "R")},
            CAGED_MAJOR_7: {6: (0, "R"), 5: (2, "5"), 4: (1, "7"), 3: (1, "3"), 2: (0, "5"), 1: (0, "R")},
            CAGED_MINOR_7: {6: (0, "R"), 5: (2, "5"), 4: (0, "b7"), 3: (0, "b3"), 2: (0, "5"), 1: (0, "R")},
            CAGED_MAJOR_6: {6: (0, "R"), 5: (2, "5"), 4: (2, "R"), 3: (1, "3"), 2: (2, "6"), 1: (0, "R")},
            CAGED_MINOR_6: {6: (0, "R"), 5: (2, "5"), 4: (2, "R"), 3: (0, "b3"), 2: (2, "6"), 1: (0, "R")},
            CAGED_SUS2: {6: (0, "R"), 5: (2, "5"), 4: (4, "2"), 3: (4, "5"), 2: (0, "5"), 1: (0, "R")},
            CAGED_SUS4: {6: (0, "R"), 5: (2, "5"), 4: (2, "R"), 3: (2, "4"), 2: (0, "5"), 1: (0, "R")},
            CAGED_ADD9: {6: (0, "R"), 5: (2, "5"), 4: (4, "9"), 3: (1, "3"), 2: (0, "5"), 1: (0, "R")},
            CAGED_DIMINISHED: {6: (0, "R"), 5: (1, "b5"), 4: (2, "R"), 3: (0, "b3")},
            CAGED_AUGMENTED: {6: (0, "R"), 5: (3, "#5"), 4: (2, "R"), 3: (1, "3"), 2: (1, "#5"), 1: (0, "R")},
        },
    },
    "CAGED D Shape": {
        "root_note": "D",
        "layouts": {
            CAGED_MAJOR: {4: (0, "R"), 3: (2, "5"), 2: (3, "R"), 1: (2, "3")},
            CAGED_MINOR: {4: (0, "R"), 3: (2, "5"), 2: (3, "R"), 1: (1, "b3")},
            CAGED_DOMINANT_7: {4: (0, "R"), 3: (2, "5"), 2: (1, "b7"), 1: (2, "3")},
            CAGED_MAJOR_7: {4: (0, "R"), 3: (2, "5"), 2: (2, "7"), 1: (2, "3")},
            CAGED_MINOR_7: {4: (0, "R"), 3: (2, "5"), 2: (1, "b7"), 1: (1, "b3")},
            CAGED_MAJOR_6: {4: (0, "R"), 3: (2, "5"), 2: (0, "6"), 1: (2, "3")},
            CAGED_MINOR_6: {4: (0, "R"), 3: (2, "5"), 2: (0, "6"), 1: (1, "b3")},
            CAGED_SUS2: {4: (0, "R"), 3: (2, "5"), 2: (3, "R"), 1: (0, "2")},
            CAGED_SUS4: {4: (0, "R"), 3: (2, "5"), 2: (3, "R"), 1: (3, "4")},
            CAGED_ADD9: {4: (0, "R"), 3: (2, "5"), 2: (3, "R"), 1: (0, "9")},
            CAGED_DIMINISHED: {4: (0, "R"), 3: (1, "b5"), 2: (3, "R"), 1: (1, "b3")},
            CAGED_AUGMENTED: {4: (0, "R"), 3: (3, "#5"), 2: (3, "R"), 1: (2, "3")},
        },
    },
}


def validate_music_data():
    """Return data-shape validation errors for chord qualities and layouts."""
    errors = []
    errors.extend(_validate_chord_qualities("drop chord quality", CHORD_QUALITIES))
    errors.extend(_validate_chord_qualities("CAGED chord quality", CAGED_CHORD_QUALITIES))
    errors.extend(_validate_drop_shapes())
    errors.extend(_validate_caged_shapes())
    errors.extend(_validate_generated_voicings())
    return errors


def get_root_notes():
    """Return the supported root notes."""
    return list(CHROMATIC_SCALE)


def get_chord_families(chord_type=None):
    """Return the supported chord quality names."""
    if chord_type in CAGED_SHAPES:
        return list(CAGED_CHORD_QUALITIES)
    return list(CHORD_QUALITIES)


def get_chord_types():
    """Return the supported drop voicing type names."""
    return list(BASE_SHAPES) + list(CAGED_SHAPES)


def get_inversions(chord_type):
    """Return inversion names for a drop voicing type."""
    if chord_type in CAGED_SHAPES:
        return [CAGED_INVERSION]
    return list(BASE_SHAPES[chord_type])


def get_voicing_note(chord_family):
    """Return the static voicing note for a supported chord quality."""
    return _chord_quality(chord_family).voicing_note


def assess_chord_playability(chord_type, inversion, chord_family, root_note):
    """Return the physical playability assessment for a selected voicing."""
    voicing = calculate_voicing(chord_type, inversion, chord_family, root_note)
    if voicing.max_note_count is None:
        return assess_playability(voicing.frets, voicing.voicing_note)
    return assess_playability(
        voicing.frets,
        voicing.voicing_note,
        max_note_count=voicing.max_note_count,
    )


def calculate_voicing(chord_type, inversion, chord_family, root_note):
    """Calculate named fretboard data for a selected guitar chord voicing."""
    if chord_type in CAGED_SHAPES:
        return _calculate_caged_voicing(chord_type, inversion, chord_family, root_note)

    root_index = CHROMATIC_SCALE.index(root_note)
    base_layout = BASE_SHAPES[chord_type][inversion]
    chord_quality = _chord_quality(chord_family, chord_type)

    positions = []

    for string, (base_fret_offset, interval_type) in base_layout.items():
        interval_modifier = chord_quality.intervals[interval_type]
        target_pitch = (root_index + interval_modifier) % SEMITONES_PER_OCTAVE
        string_open_pitch = STRING_TUNING_OFFSETS[string]

        fret = (target_pitch - string_open_pitch) % SEMITONES_PER_OCTAVE
        if fret < LOW_FRET_WRAP_LIMIT and base_fret_offset > UPPER_SHAPE_OFFSET_THRESHOLD:
            fret += SEMITONES_PER_OCTAVE
        elif base_fret_offset >= HIGH_POSITION_OFFSET_THRESHOLD and fret < HIGH_POSITION_WRAP_LIMIT:
            fret += SEMITONES_PER_OCTAVE

        positions.append(
            FretPosition(
                string=string,
                fret=fret,
                label=chord_quality.display_labels[interval_type],
            )
        )

    return VoicingResult(
        chord_type=chord_type,
        inversion=inversion,
        chord_family=chord_family,
        root_note=root_note,
        positions=tuple(positions),
        voicing_note=chord_quality.voicing_note,
    )


def calculate_fret_positions(chord_type, inversion, chord_family, root_note):
    """Calculate fret positions for a selected guitar chord voicing."""
    voicing = calculate_voicing(chord_type, inversion, chord_family, root_note)
    return voicing.frets, voicing.labels


def _calculate_caged_voicing(chord_type, inversion, chord_family, root_note):
    root_index = CHROMATIC_SCALE.index(root_note)
    shape = CAGED_SHAPES[chord_type]
    shape_root_index = CHROMATIC_SCALE.index(shape["root_note"])
    shape_offset = (root_index - shape_root_index) % SEMITONES_PER_OCTAVE
    chord_quality = _chord_quality(chord_family, chord_type)
    layout = shape["layouts"][chord_family]

    positions = []

    for string, (base_fret, interval_type) in layout.items():
        interval_modifier = chord_quality.intervals[interval_type]
        target_pitch = (root_index + interval_modifier) % SEMITONES_PER_OCTAVE
        preferred_fret = base_fret + shape_offset

        positions.append(
            FretPosition(
                string=string,
                fret=_nearest_fret_for_pitch(string, target_pitch, preferred_fret),
                label=chord_quality.display_labels[interval_type],
            )
        )

    return VoicingResult(
        chord_type=chord_type,
        inversion=inversion,
        chord_family=chord_family,
        root_note=root_note,
        positions=tuple(positions),
        voicing_note=chord_quality.voicing_note,
        max_note_count=MAX_NOTES_IN_CAGED_MODEL,
    )


def _nearest_fret_for_pitch(string, target_pitch, preferred_fret):
    base_fret = (target_pitch - STRING_TUNING_OFFSETS[string]) % SEMITONES_PER_OCTAVE
    candidates = [
        base_fret + (SEMITONES_PER_OCTAVE * octave)
        for octave in range(CAGED_FRET_SEARCH_OCTAVES)
    ]
    return min(candidates, key=lambda fret: abs(fret - preferred_fret))


def _chord_quality(chord_family, chord_type=None):
    if chord_type in CAGED_SHAPES and chord_family in CAGED_CHORD_QUALITIES:
        return CAGED_CHORD_QUALITIES[chord_family]
    if chord_family in CHORD_QUALITIES:
        return CHORD_QUALITIES[chord_family]
    return CAGED_CHORD_QUALITIES[chord_family]


def _validate_chord_qualities(label, qualities):
    errors = []
    for name, quality in qualities.items():
        interval_keys = set(quality.intervals)
        display_keys = set(quality.display_labels)
        if interval_keys != display_keys:
            errors.append(
                f"{label} {name!r} has interval keys {sorted(interval_keys)} "
                f"but display-label keys {sorted(display_keys)}."
            )
        if "R" not in interval_keys:
            errors.append(f"{label} {name!r} does not define a root interval.")
    return errors


def _validate_drop_shapes():
    errors = []
    for chord_type, inversions in BASE_SHAPES.items():
        if not inversions:
            errors.append(f"{chord_type!r} has no inversions.")
        for inversion, layout in inversions.items():
            context = f"{chord_type!r} {inversion!r}"
            errors.extend(_validate_layout(context, layout, CHORD_QUALITIES))
    return errors


def _validate_caged_shapes():
    errors = []
    for chord_type, shape in CAGED_SHAPES.items():
        root_note = shape.get("root_note")
        if root_note not in CHROMATIC_SCALE:
            errors.append(f"{chord_type!r} has unsupported root note {root_note!r}.")

        layouts = shape.get("layouts", {})
        layout_names = set(layouts)
        quality_names = set(CAGED_CHORD_QUALITIES)
        missing = quality_names - layout_names
        extra = layout_names - quality_names
        if missing:
            errors.append(f"{chord_type!r} is missing CAGED layouts for {sorted(missing)}.")
        if extra:
            errors.append(f"{chord_type!r} has unsupported CAGED layouts for {sorted(extra)}.")

        for chord_family, layout in layouts.items():
            context = f"{chord_type!r} {chord_family!r}"
            quality = CAGED_CHORD_QUALITIES.get(chord_family)
            if quality is None:
                continue
            errors.extend(_validate_layout(context, layout, {chord_family: quality}))
    return errors


def _validate_layout(context, layout, qualities):
    errors = []
    if not layout:
        return [f"{context} has no string layout."]

    for string, note in layout.items():
        if string not in STRING_TUNING_OFFSETS:
            errors.append(f"{context} uses unsupported string {string!r}.")
            continue
        try:
            fret, interval_type = note
        except (TypeError, ValueError):
            errors.append(f"{context} string {string} has invalid note data {note!r}.")
            continue
        if not isinstance(fret, int) or fret < 0:
            errors.append(f"{context} string {string} has invalid fret {fret!r}.")
        for quality_name, quality in qualities.items():
            if interval_type not in quality.intervals:
                errors.append(
                    f"{context} string {string} uses interval {interval_type!r}, "
                    f"missing from {quality_name!r} intervals."
                )
            if interval_type not in quality.display_labels:
                errors.append(
                    f"{context} string {string} uses interval {interval_type!r}, "
                    f"missing from {quality_name!r} display labels."
                )
    return errors


def _validate_generated_voicings():
    errors = []
    for root_note in CHROMATIC_SCALE:
        for chord_type in get_chord_types():
            for chord_family in get_chord_families(chord_type):
                for inversion in get_inversions(chord_type):
                    context = f"{root_note} {chord_family} {chord_type} {inversion}"
                    try:
                        voicing = calculate_voicing(chord_type, inversion, chord_family, root_note)
                    except (KeyError, ValueError) as error:
                        errors.append(f"{context} failed to calculate: {error}.")
                        continue
                    if not voicing.positions:
                        errors.append(f"{context} generated no fret positions.")
                    if set(voicing.frets) != set(voicing.labels):
                        errors.append(f"{context} generated mismatched fret and label strings.")
                    for position in voicing.positions:
                        if position.string not in STRING_TUNING_OFFSETS:
                            errors.append(f"{context} generated unsupported string {position.string!r}.")
                        if position.fret < 0:
                            errors.append(f"{context} generated negative fret {position.fret}.")
                        if not position.label:
                            errors.append(f"{context} generated an empty label.")
    return errors


_MUSIC_DATA_ERRORS = validate_music_data()
if _MUSIC_DATA_ERRORS:
    raise ValueError("Invalid music data:\n" + "\n".join(_MUSIC_DATA_ERRORS))
