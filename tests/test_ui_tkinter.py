"""Tests for Tkinter UI helpers."""

from pathlib import Path
import sys
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

from guitar_chords_viewer.music_theory import (
    FretPosition,
    VoicingResult,
    calculate_voicing,
    get_chord_families,
    get_chord_types,
    get_inversions,
    get_root_notes,
)
from guitar_chords_viewer.ui_tkinter import CHORD_SYMBOL_SUFFIXES, centered_geometry, compact_chord_name


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

    def test_compact_chord_name_uses_common_minor_seventh_symbol(self):
        voicing = calculate_voicing(
            "CAGED E Shape",
            "Standard Shape",
            "Minor 7 (R-b3-5-b7)",
            "C",
        )

        self.assertEqual(compact_chord_name(voicing), "Cm7")

    def test_compact_chord_name_does_not_add_slash_for_root_position_open_strings(self):
        voicing = calculate_voicing(
            "Drop 2",
            "Root Position",
            "Major 7 (R-3-5-7)",
            "C",
        )

        self.assertEqual(compact_chord_name(voicing), "Cmaj7")

    def test_compact_chord_name_uses_common_minor_major_seventh_symbol(self):
        voicing = VoicingResult(
            chord_type="Test Shape",
            inversion="Test Inversion",
            chord_family="Minor Major 7 (R-b3-5-7)",
            root_note="C",
            positions=(
                FretPosition(string=5, fret=3, label="R"),
                FretPosition(string=4, fret=1, label="b3"),
                FretPosition(string=3, fret=0, label="5"),
                FretPosition(string=2, fret=0, label="7"),
            ),
            voicing_note="Test root-position minor-major seventh voicing.",
        )

        self.assertEqual(compact_chord_name(voicing), "CmMaj7")

    def test_compact_chord_name_adds_slash_bass_for_inverted_voicing(self):
        voicing = VoicingResult(
            chord_type="Test Shape",
            inversion="Test Inversion",
            chord_family="Minor triad (R-b3-5)",
            root_note="C",
            positions=(
                FretPosition(string=3, fret=0, label="5"),
                FretPosition(string=2, fret=1, label="R"),
                FretPosition(string=1, fret=3, label="b3"),
            ),
            voicing_note="Test voicing with G in the bass.",
        )

        self.assertEqual(compact_chord_name(voicing), "Cm/G")

    def test_compact_chord_name_spells_flat_third_bass(self):
        voicing = calculate_voicing(
            "Drop 2",
            "1st Inversion",
            "Minor 7 (R-b3-5-b7)",
            "C",
        )

        self.assertEqual(compact_chord_name(voicing), "Cm7/Eb")

    def test_compact_chord_name_spells_flat_seventh_bass(self):
        voicing = calculate_voicing(
            "Drop 2",
            "3rd Inversion",
            "Dominant 7 (R-3-5-b7)",
            "C",
        )

        self.assertEqual(compact_chord_name(voicing), "C7/Bb")

    def test_compact_chord_name_spells_sharp_fifth_bass(self):
        voicing = calculate_voicing(
            "Drop 2",
            "2nd Inversion",
            "Augmented Major 7 (R-3-#5-7)",
            "C",
        )

        self.assertEqual(compact_chord_name(voicing), "CaugMaj7/G#")

    def test_compact_chord_name_supports_every_available_chord_quality(self):
        chord_families = {
            chord_family
            for chord_type in get_chord_types()
            for chord_family in get_chord_families(chord_type)
        }

        for chord_family in chord_families:
            with self.subTest(chord_family=chord_family):
                voicing = VoicingResult(
                    chord_type="Test Shape",
                    inversion="Test Inversion",
                    chord_family=chord_family,
                    root_note="C",
                    positions=(FretPosition(string=5, fret=3, label="R"),),
                    voicing_note="Test root-position voicing.",
                )

                self.assertTrue(compact_chord_name(voicing).startswith("C"))

    def test_compact_chord_name_uses_plain_quality_for_root_positions(self):
        for root_note in get_root_notes():
            for chord_type in get_chord_types():
                for chord_family in get_chord_families(chord_type):
                    for inversion in get_inversions(chord_type):
                        if inversion not in {"Root Position", "Standard Shape"}:
                            continue
                        with self.subTest(
                            root_note=root_note,
                            chord_type=chord_type,
                            chord_family=chord_family,
                            inversion=inversion,
                        ):
                            voicing = calculate_voicing(chord_type, inversion, chord_family, root_note)

                            self.assertEqual(
                                compact_chord_name(voicing),
                                f"{root_note}{CHORD_SYMBOL_SUFFIXES[chord_family]}",
                            )

    def test_compact_chord_name_avoids_double_accidental_bass_names(self):
        for root_note in get_root_notes():
            for chord_type in get_chord_types():
                for chord_family in get_chord_families(chord_type):
                    for inversion in get_inversions(chord_type):
                        with self.subTest(
                            root_note=root_note,
                            chord_type=chord_type,
                            chord_family=chord_family,
                            inversion=inversion,
                        ):
                            voicing = calculate_voicing(chord_type, inversion, chord_family, root_note)
                            chord_name = compact_chord_name(voicing)

                            self.assertNotIn("##", chord_name)
                            self.assertNotIn("bb", chord_name)


if __name__ == "__main__":
    unittest.main()
