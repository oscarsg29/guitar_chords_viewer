"""Tests for guitar playability rules."""

from pathlib import Path
import sys
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

from guitar_chords_viewer.playability import EASY, NOT_RECOMMENDED, STRETCHY, assess_playability


class PlayabilityTests(unittest.TestCase):
    def test_easy_grip_has_small_fret_span(self):
        assessment = assess_playability({4: 5, 3: 6, 2: 7, 1: 8}, "Test voicing.")

        self.assertEqual(assessment.rating, EASY)
        self.assertEqual(assessment.fret_span, 3)

    def test_stretchy_grip_has_medium_fret_span(self):
        assessment = assess_playability({4: 5, 3: 7, 2: 9, 1: 10}, "Test voicing.")

        self.assertEqual(assessment.rating, STRETCHY)
        self.assertEqual(assessment.fret_span, 5)

    def test_wide_grip_is_not_recommended(self):
        assessment = assess_playability({4: 2, 3: 5, 2: 8, 1: 9}, "Test voicing.")

        self.assertEqual(assessment.rating, NOT_RECOMMENDED)
        self.assertEqual(assessment.fret_span, 7)

    def test_open_strings_do_not_count_against_fret_span(self):
        assessment = assess_playability({4: 0, 3: 0, 2: 2, 1: 3}, "Test voicing.")

        self.assertEqual(assessment.rating, EASY)
        self.assertEqual(assessment.fret_span, 1)


if __name__ == "__main__":
    unittest.main()
