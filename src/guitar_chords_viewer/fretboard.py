"""Fretboard layout constants and drawing helpers."""

CANVAS_BACKGROUND = "#111111"
FRET_COLOR = "#555555"
NUT_COLOR = "#f4f4f4"
STRING_COLOR = "#9a9a9a"
TEXT_COLOR = "#dddddd"
ROOT_MARKER_COLOR = "#00A85A"
TONE_MARKER_COLOR = "#2F72D6"
MARKER_OUTLINE_COLOR = "white"
MARKER_TEXT_COLOR = "white"
MARKER_RADIUS = 17
MARKER_OUTLINE_WIDTH = 2
MARKER_FONT = ("Helvetica", 11, "bold")

MIN_CANVAS_WIDTH = 700
MIN_CANVAS_HEIGHT = 300
MARGIN_LEFT = 72
MARGIN_RIGHT = 28
MARGIN_TOP = 42
MARGIN_BOTTOM = 52
FIRST_STRING = 1
LAST_STRING = 6
STRING_GAP_COUNT = LAST_STRING - FIRST_STRING

GRID_MIN_FRET = 0
MIN_VISIBLE_FRET_SPAN = 4
FRET_PADDING_BEFORE = 1
FRET_PADDING_AFTER = 2
NUT_FRET = 0
NUT_LINE_WIDTH = 6
FRET_LINE_WIDTH = 2
FRET_LABEL_X_OFFSET = 4
FRET_LABEL_BOTTOM_OFFSET = 24

STRING_BASE_WIDTH = 1
LOW_STRING_WIDTH_REFERENCE = 6
STRING_WIDTH_STEP = 0.45
STRING_LABEL_X_OFFSET = 18


def fret_grid_bounds(frets):
    """Return the visible fret range needed for a voicing."""
    return (
        max(GRID_MIN_FRET, min(frets) - FRET_PADDING_BEFORE),
        max(MIN_VISIBLE_FRET_SPAN, max(frets) + FRET_PADDING_AFTER),
    )


def fret_x(fret, min_grid, fret_width):
    """Return the canvas x-coordinate for a fret."""
    return MARGIN_LEFT + (fret - min_grid) * fret_width


def string_y(string, string_gap):
    """Return the canvas y-coordinate for a string number."""
    return MARGIN_TOP + (string - 1) * string_gap


def marker_color(interval_label):
    """Return the note marker color for an interval label."""
    if interval_label == "R":
        return ROOT_MARKER_COLOR
    return TONE_MARKER_COLOR
