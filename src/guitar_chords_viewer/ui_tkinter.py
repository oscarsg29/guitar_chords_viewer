"""Tkinter user interface for the guitar chord viewer."""

from pathlib import Path
import subprocess
import tkinter as tk
from tkinter import ttk

from guitar_chords_viewer.audio import PLAY_MODE_CHORD, PLAY_MODES, play_frets
from guitar_chords_viewer.fretboard import (
    CANVAS_BACKGROUND,
    FIRST_STRING,
    FRET_COLOR,
    FRET_LABEL_BOTTOM_OFFSET,
    FRET_LABEL_X_OFFSET,
    FRET_LINE_WIDTH,
    LAST_STRING,
    LOW_STRING_WIDTH_REFERENCE,
    MARGIN_BOTTOM,
    MARGIN_LEFT,
    MARGIN_RIGHT,
    MARGIN_TOP,
    MARKER_FONT,
    MARKER_OUTLINE_COLOR,
    MARKER_OUTLINE_WIDTH,
    MARKER_RADIUS,
    MARKER_TEXT_COLOR,
    MIN_CANVAS_HEIGHT,
    MIN_CANVAS_WIDTH,
    NUT_FRET,
    NUT_COLOR,
    NUT_LINE_WIDTH,
    STRING_BASE_WIDTH,
    STRING_COLOR,
    STRING_GAP_COUNT,
    STRING_LABEL_X_OFFSET,
    STRING_WIDTH_STEP,
    TEXT_COLOR,
    fret_grid_bounds,
    fret_x,
    marker_color,
    note_marker_x,
    string_y,
)
from guitar_chords_viewer.music_theory import (
    CHROMATIC_SCALE,
    STRING_NAMES,
    calculate_voicing,
    get_chord_families,
    get_chord_types,
    get_inversions,
    get_root_notes,
)


APP_TITLE = "Guitar Chords Visualizer"
AUTHOR_NAME = "Oscar Osorio"
AUTHOR_INSTAGRAM = "bones29sg"
DEFAULT_WINDOW_WIDTH = 1280
DEFAULT_WINDOW_HEIGHT = 720
DEFAULT_WINDOW_SIZE = f"{DEFAULT_WINDOW_WIDTH}x{DEFAULT_WINDOW_HEIGHT}"
MIN_WINDOW_WIDTH = 1180
MIN_WINDOW_HEIGHT = 620
SCREEN_ORIGIN = 0
ALWAYS_ON_TOP = True
FIRST_OPTION_INDEX = 0

HEADER_PADDING = (18, 14, 18, 8)
BODY_PADDING = (18, 8, 18, 14)
FOOTER_PADDING = (18, 0, 18, 12)
INSTAGRAM_ICON_SIZE = 18
INSTAGRAM_ICON_STROKE = "#202124"
TITLE_FONT = ("Helvetica", 20, "bold")
TITLE_ROW = 0
CONTROLS_ROW = 1
GROUP_CONTROLS_ROW = 0
FIRST_CONTROL_COLUMN = 0
CONTROL_COLUMN_PADDING = 8
CONTROL_COLUMN_COUNT = 3
TITLE_COLUMNSPAN = CONTROL_COLUMN_COUNT
TITLE_BOTTOM_PADDING = 10
SELECTOR_TOP_PADDING = 4
GROUP_INNER_PADDING = 10
INFO_WRAP_LENGTH = 260

KEY_ROOT_COLUMN = 0
CHORD_QUALITY_COLUMN = 1
DROP_TYPE_COLUMN = 2
INVERSION_COLUMN = 3
PLAYBACK_COLUMN = 1
INFO_COLUMN = 2
CHORD_CONTROL_COLUMN_COUNT = 4

CHORD_SYMBOL_SUFFIXES = {
    "Major triad (R-3-5)": "",
    "Minor triad (R-b3-5)": "m",
    "Dominant 7 (R-3-5-b7)": "7",
    "Major 7 (R-3-5-7)": "maj7",
    "Minor 7 (R-b3-5-b7)": "m7",
    "Major 6 (R-3-5-6)": "6",
    "Minor 6 (R-b3-5-6)": "m6",
    "Suspended 2 (R-2-5)": "sus2",
    "Suspended 4 (R-4-5)": "sus4",
    "Add 9 (R-3-5-9)": "add9",
    "Diminished triad (R-b3-b5)": "dim",
    "Augmented triad (R-3-#5)": "aug",
    "Minor 7 b5 (R-b3-b5-b7)": "m7b5",
    "Diminished 7 (R-b3-b5-bb7)": "dim7",
    "Minor Major 7 (R-b3-5-7)": "mMaj7",
    "Augmented Major 7 (R-3-#5-7)": "augMaj7",
    "Augmented Dominant 7 (R-3-#5-b7)": "aug7",
    "Dominant 7 b5 (R-3-b5-b7)": "7b5",
    "Dominant 7 #5 (R-3-#5-b7)": "7#5",
    "Dominant 7 sus4 (R-4-5-b7)": "7sus4",
    "Major 7 #11 shell (R-3-7-#11)": "maj7#11",
    "Dominant 9 shell (R-3-b7-9)": "9",
    "Minor 9 shell (R-b3-b7-9)": "m9",
    "Major 9 shell (R-3-7-9)": "maj9",
    "6/9 shell (R-3-6-9)": "6/9",
    "Minor 6/9 shell (R-b3-6-9)": "m6/9",
    "9sus4 shell (R-4-b7-9)": "9sus4",
    "Dominant 13 shell (R-3-b7-13)": "13",
    "Minor 11 shell (R-b3-b7-11)": "m11",
}

NATURAL_NOTE_PITCHES = {
    "C": 0,
    "D": 2,
    "E": 4,
    "F": 5,
    "G": 7,
    "A": 9,
    "B": 11,
}
NATURAL_NOTES = list(NATURAL_NOTE_PITCHES)
INTERVAL_SEMITONES = {
    "R": 0,
    "2": 2,
    "b3": 3,
    "3": 4,
    "4": 5,
    "b5": 6,
    "#5": 8,
    "5": 7,
    "6": 9,
    "bb7": 9,
    "b7": 10,
    "7": 11,
    "9": 14,
    "11": 17,
    "#11": 18,
    "13": 21,
}
INTERVAL_LETTER_STEPS = {
    "R": 0,
    "2": 1,
    "9": 1,
    "b3": 2,
    "3": 2,
    "4": 3,
    "11": 3,
    "#11": 3,
    "b5": 4,
    "5": 4,
    "#5": 4,
    "6": 5,
    "13": 5,
    "bb7": 6,
    "b7": 6,
    "7": 6,
}


def centered_geometry(window_width, window_height, screen_width, screen_height):
    """Return a Tk geometry string centered within the available screen."""
    left = max(SCREEN_ORIGIN, (screen_width - window_width) // 2)
    top = max(SCREEN_ORIGIN, (screen_height - window_height) // 2)
    return f"{window_width}x{window_height}+{left}+{top}"


def current_version_label():
    """Return a short git commit label when the app is running from a checkout."""
    project_root = Path(__file__).resolve().parents[2]
    try:
        commit = subprocess.check_output(
            ["git", "-C", str(project_root), "rev-parse", "--short", "HEAD"],
            stderr=subprocess.DEVNULL,
            text=True,
            timeout=1,
        ).strip()
    except (OSError, subprocess.SubprocessError):
        return "local build"
    return f"commit {commit}" if commit else "local build"


def compact_chord_name(voicing):
    """Return a lead-sheet style chord symbol for the selected voicing."""
    suffix = CHORD_SYMBOL_SUFFIXES[voicing.chord_family]
    chord_name = f"{voicing.root_note}{suffix}"
    bass_note = _bass_note_name(voicing)
    if bass_note != voicing.root_note:
        return f"{chord_name}/{bass_note}"
    return chord_name


def _bass_note_name(voicing):
    bass_position = max(voicing.positions, key=lambda position: position.string)
    return _spell_chord_tone(voicing.root_note, bass_position.label)


def _spell_chord_tone(root_note, interval_label):
    if interval_label == "R":
        return root_note

    root_pitch = CHROMATIC_SCALE.index(root_note)
    target_pitch = (root_pitch + INTERVAL_SEMITONES[interval_label]) % len(CHROMATIC_SCALE)
    target_letter = _interval_letter(root_note, interval_label)
    target_natural_pitch = NATURAL_NOTE_PITCHES[target_letter]
    accidental_offset = target_pitch - target_natural_pitch
    if accidental_offset > len(CHROMATIC_SCALE) // 2:
        accidental_offset -= len(CHROMATIC_SCALE)
    elif accidental_offset < -(len(CHROMATIC_SCALE) // 2):
        accidental_offset += len(CHROMATIC_SCALE)

    if abs(accidental_offset) > 1:
        return CHROMATIC_SCALE[target_pitch]

    if accidental_offset < 0:
        accidental = "b" * abs(accidental_offset)
    else:
        accidental = "#" * accidental_offset
    return f"{target_letter}{accidental}"


def _interval_letter(root_note, interval_label):
    root_letter = root_note[0]
    root_letter_index = NATURAL_NOTES.index(root_letter)
    target_letter_index = (root_letter_index + INTERVAL_LETTER_STEPS[interval_label]) % len(NATURAL_NOTES)
    return NATURAL_NOTES[target_letter_index]


class GuitarChordViewer(tk.Tk):
    """Desktop app for selecting and drawing guitar drop chord voicings."""

    def __init__(self):
        super().__init__()
        self._configure_window()

        chord_type = get_chord_types()[FIRST_OPTION_INDEX]
        chord_family = get_chord_families(chord_type)[FIRST_OPTION_INDEX]
        self.root_note = tk.StringVar(value=get_root_notes()[FIRST_OPTION_INDEX])
        self.chord_family = tk.StringVar(value=chord_family)
        self.chord_type = tk.StringVar(value=chord_type)
        self.inversion = tk.StringVar(value=get_inversions(chord_type)[FIRST_OPTION_INDEX])
        self.play_mode = tk.StringVar(value=PLAY_MODE_CHORD)
        self.chord_name = tk.StringVar()
        self.footer = tk.StringVar(
            value=(
                f"Version: {current_version_label()} | Author: {AUTHOR_NAME}"
            )
        )

        self._build_controls()
        self._build_canvas()
        self._build_footer()
        self._bind_updates()
        self.draw_fretboard()

    def _configure_window(self):
        self.title(APP_TITLE)
        self.geometry(
            centered_geometry(
                DEFAULT_WINDOW_WIDTH,
                DEFAULT_WINDOW_HEIGHT,
                self.winfo_screenwidth(),
                self.winfo_screenheight(),
            )
        )
        self.minsize(MIN_WINDOW_WIDTH, MIN_WINDOW_HEIGHT)
        self.attributes("-topmost", ALWAYS_ON_TOP)

    def _build_controls(self):
        header = ttk.Frame(self, padding=HEADER_PADDING)
        header.pack(fill=tk.X)

        title = ttk.Label(header, text=APP_TITLE, font=TITLE_FONT)
        title.grid(
            row=TITLE_ROW,
            column=FIRST_CONTROL_COLUMN,
            columnspan=TITLE_COLUMNSPAN,
            sticky="w",
            pady=(0, TITLE_BOTTOM_PADDING),
        )

        chord_group = ttk.LabelFrame(header, text="Chord", padding=GROUP_INNER_PADDING)
        chord_group.grid(row=CONTROLS_ROW, column=FIRST_CONTROL_COLUMN, sticky="nsew")
        self._add_selector(chord_group, "Key Root", self.root_note, get_root_notes(), KEY_ROOT_COLUMN)
        self.chord_family_menu = self._add_selector(
            chord_group,
            "Chord Quality",
            self.chord_family,
            get_chord_families(self.chord_type.get()),
            CHORD_QUALITY_COLUMN,
        )
        self._add_selector(chord_group, "Drop Type", self.chord_type, get_chord_types(), DROP_TYPE_COLUMN)
        self.inversion_menu = self._add_selector(
            chord_group,
            "Inversion",
            self.inversion,
            get_inversions(self.chord_type.get()),
            INVERSION_COLUMN,
        )
        for column in range(CHORD_CONTROL_COLUMN_COUNT):
            chord_group.columnconfigure(column, weight=1)

        playback_group = ttk.LabelFrame(header, text="Playback", padding=GROUP_INNER_PADDING)
        playback_group.grid(
            row=CONTROLS_ROW,
            column=PLAYBACK_COLUMN,
            sticky="nsew",
            padx=(CONTROL_COLUMN_PADDING, 0),
        )
        self._add_selector(playback_group, "Play Mode", self.play_mode, PLAY_MODES, FIRST_CONTROL_COLUMN)
        self._add_play_button(playback_group)

        info_group = ttk.LabelFrame(header, text="Info", padding=GROUP_INNER_PADDING)
        info_group.grid(row=CONTROLS_ROW, column=INFO_COLUMN, sticky="nsew", padx=(CONTROL_COLUMN_PADDING, 0))
        ttk.Label(info_group, textvariable=self.chord_name, font=("Helvetica", 15, "bold")).pack(anchor="w")

        header.columnconfigure(FIRST_CONTROL_COLUMN, weight=5)
        header.columnconfigure(PLAYBACK_COLUMN, weight=2)
        header.columnconfigure(INFO_COLUMN, weight=3)

    def _add_selector(self, parent, label_text, variable, values, column):
        frame = ttk.Frame(parent)
        left_padding = 0 if column == FIRST_CONTROL_COLUMN else CONTROL_COLUMN_PADDING
        frame.grid(row=GROUP_CONTROLS_ROW, column=column, sticky="ew", padx=(left_padding, 0))

        ttk.Label(frame, text=label_text).pack(anchor="w")
        menu = ttk.OptionMenu(frame, variable, variable.get(), *values)
        menu.pack(fill=tk.X, pady=(SELECTOR_TOP_PADDING, 0))
        return menu

    def _add_play_button(self, parent):
        frame = ttk.Frame(parent)
        frame.grid(row=GROUP_CONTROLS_ROW, column=1, sticky="ew", padx=(CONTROL_COLUMN_PADDING, 0))

        ttk.Label(frame, text="Audio").pack(anchor="w")
        button = ttk.Button(frame, text="▶ Play", command=self._play_selected_chord)
        button.pack(fill=tk.X, pady=(SELECTOR_TOP_PADDING, 0))

    def _build_canvas(self):
        body = ttk.Frame(self, padding=BODY_PADDING)
        body.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(body, background=CANVAS_BACKGROUND, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<Configure>", lambda _event: self.draw_fretboard())

    def _build_footer(self):
        footer = ttk.Frame(self, padding=FOOTER_PADDING)
        footer.pack(fill=tk.X)
        ttk.Label(footer, textvariable=self.footer).pack(side=tk.LEFT)
        self._add_instagram_icon(footer)
        ttk.Label(footer, text=f"@{AUTHOR_INSTAGRAM}").pack(side=tk.LEFT, padx=(4, 0))

    def _add_instagram_icon(self, parent):
        icon = tk.Canvas(
            parent,
            width=INSTAGRAM_ICON_SIZE,
            height=INSTAGRAM_ICON_SIZE,
            highlightthickness=0,
        )
        icon.pack(side=tk.LEFT, padx=(8, 0))
        icon.create_rectangle(
            2,
            2,
            INSTAGRAM_ICON_SIZE - 2,
            INSTAGRAM_ICON_SIZE - 2,
            outline=INSTAGRAM_ICON_STROKE,
            width=2,
        )
        icon.create_oval(6, 6, INSTAGRAM_ICON_SIZE - 6, INSTAGRAM_ICON_SIZE - 6, outline=INSTAGRAM_ICON_STROKE, width=2)
        icon.create_oval(13, 4, 15, 6, fill=INSTAGRAM_ICON_STROKE, outline=INSTAGRAM_ICON_STROKE)

    def _bind_updates(self):
        for variable in (self.root_note, self.chord_family, self.chord_type, self.inversion):
            variable.trace_add("write", lambda *_args: self._selection_changed())

    def _selection_changed(self):
        self._refresh_chord_families()
        self._refresh_inversions()
        self.draw_fretboard()

    def _refresh_chord_families(self):
        valid_chord_families = get_chord_families(self.chord_type.get())
        if self.chord_family.get() not in valid_chord_families:
            self.chord_family.set(valid_chord_families[FIRST_OPTION_INDEX])

        menu = self.chord_family_menu["menu"]
        menu.delete(0, "end")
        for value in valid_chord_families:
            menu.add_command(label=value, command=tk._setit(self.chord_family, value))

    def _play_selected_chord(self):
        voicing = calculate_voicing(
            self.chord_type.get(),
            self.inversion.get(),
            self.chord_family.get(),
            self.root_note.get(),
        )
        play_frets(voicing.frets, play_mode=self.play_mode.get())

    def _refresh_inversions(self):
        valid_inversions = get_inversions(self.chord_type.get())
        if self.inversion.get() not in valid_inversions:
            self.inversion.set(valid_inversions[FIRST_OPTION_INDEX])

        menu = self.inversion_menu["menu"]
        menu.delete(0, "end")
        for value in valid_inversions:
            menu.add_command(label=value, command=tk._setit(self.inversion, value))

    def draw_fretboard(self):
        if not hasattr(self, "canvas"):
            return

        voicing = calculate_voicing(
            self.chord_type.get(),
            self.inversion.get(),
            self.chord_family.get(),
            self.root_note.get(),
        )
        self._draw_fretboard(voicing)
        self._update_status(voicing)

    def _draw_fretboard(self, voicing):
        width = max(self.canvas.winfo_width(), MIN_CANVAS_WIDTH)
        height = max(self.canvas.winfo_height(), MIN_CANVAS_HEIGHT)
        min_grid, max_grid = fret_grid_bounds(voicing.frets.values())
        fret_count = max_grid - min_grid
        fret_width = (width - MARGIN_LEFT - MARGIN_RIGHT) / fret_count
        string_gap = (height - MARGIN_TOP - MARGIN_BOTTOM) / STRING_GAP_COUNT

        self.canvas.delete("all")
        self._draw_frets(height, min_grid, max_grid, fret_width)
        self._draw_strings(width, string_gap)
        self._draw_markers(voicing, min_grid, fret_width, string_gap)

    def _draw_frets(self, height, min_grid, max_grid, fret_width):
        for fret in range(min_grid, max_grid + 1):
            x = fret_x(fret, min_grid, fret_width)
            color = NUT_COLOR if fret == NUT_FRET else FRET_COLOR
            line_width = NUT_LINE_WIDTH if fret == NUT_FRET else FRET_LINE_WIDTH
            self.canvas.create_line(x, MARGIN_TOP, x, height - MARGIN_BOTTOM, fill=color, width=line_width)
            if fret == NUT_FRET:
                continue
            self.canvas.create_text(
                x + FRET_LABEL_X_OFFSET,
                height - FRET_LABEL_BOTTOM_OFFSET,
                text=str(fret),
                fill=TEXT_COLOR,
                anchor="w",
            )

    def _draw_strings(self, width, string_gap):
        for string in range(FIRST_STRING, LAST_STRING + 1):
            y = string_y(string, string_gap)
            line_width = STRING_BASE_WIDTH + (LOW_STRING_WIDTH_REFERENCE - string) * STRING_WIDTH_STEP
            self.canvas.create_line(MARGIN_LEFT, y, width - MARGIN_RIGHT, y, fill=STRING_COLOR, width=line_width)
            self.canvas.create_text(
                MARGIN_LEFT - STRING_LABEL_X_OFFSET,
                y,
                text=STRING_NAMES[string],
                fill=TEXT_COLOR,
                anchor="e",
            )

    def _draw_markers(self, voicing, min_grid, fret_width, string_gap):
        for position in voicing.positions:
            x = note_marker_x(position.fret, min_grid, fret_width)
            y = string_y(position.string, string_gap)
            self.canvas.create_oval(
                x - MARKER_RADIUS,
                y - MARKER_RADIUS,
                x + MARKER_RADIUS,
                y + MARKER_RADIUS,
                fill=marker_color(position.label),
                outline=MARKER_OUTLINE_COLOR,
                width=MARKER_OUTLINE_WIDTH,
            )
            self.canvas.create_text(
                x,
                y,
                text=position.label,
                fill=MARKER_TEXT_COLOR,
                font=MARKER_FONT,
            )

    def _update_status(self, voicing):
        self.chord_name.set(compact_chord_name(voicing))
