"""Tests for Tkinter UI helpers."""

from pathlib import Path
import sys
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

from guitar_chords_viewer.ui_tkinter import centered_geometry


class TkinterUiTests(unittest.TestCase):
    def test_centered_geometry_centers_window_on_larger_screen(self):
        geometry = centered_geometry(
            window_width=920,
            window_height=560,
            screen_width=1920,
            screen_height=1080,
        )

        self.assertEqual(geometry, "920x560+500+260")

    def test_centered_geometry_keeps_window_on_screen_when_screen_is_smaller(self):
        geometry = centered_geometry(
            window_width=920,
            window_height=560,
            screen_width=800,
            screen_height=500,
        )

        self.assertEqual(geometry, "920x560+0+0")


if __name__ == "__main__":
    unittest.main()
