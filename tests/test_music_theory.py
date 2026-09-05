"""Tests for pure music-theory logic."""

from pathlib import Path
import sys
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

from guitar_chords_viewer.music_theory import (
    calculate_fret_positions,
    get_chord_families,
    get_chord_types,
    get_inversions,
    get_root_notes,
)


class MusicTheoryTests(unittest.TestCase):
    def test_calculate_c_major_7_drop_2_root_position(self):
        frets, labels = calculate_fret_positions(
            "Drop 2",
            "Root Position",
            "Major 7 (R-3-5-7)",
            "C",
        )

        self.assertEqual(frets, {4: 10, 3: 0, 2: 0, 1: 0})
        self.assertEqual(labels, {4: "R", 3: "5", 2: "7", 1: "3"})

    def test_selection_lists_are_not_empty(self):
        self.assertGreater(len(get_root_notes()), 0)
        self.assertGreater(len(get_chord_families()), 0)
        self.assertGreater(len(get_chord_types()), 0)
        self.assertGreater(len(get_inversions("Drop 2")), 0)


if __name__ == "__main__":
    unittest.main()
