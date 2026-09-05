"""Tests for fretboard coordinate helpers."""

from pathlib import Path
import sys
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

from guitar_chords_viewer.fretboard import MARGIN_LEFT, note_marker_x


class FretboardTests(unittest.TestCase):
    def test_fretted_note_marker_is_behind_fret_line(self):
        fret_width = 20

        self.assertEqual(note_marker_x(fret=3, min_grid=0, fret_width=fret_width), MARGIN_LEFT + 50)

    def test_open_note_marker_is_after_nut_line(self):
        fret_width = 20

        self.assertEqual(note_marker_x(fret=0, min_grid=0, fret_width=fret_width), MARGIN_LEFT + 10)


if __name__ == "__main__":
    unittest.main()
