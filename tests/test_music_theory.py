"""Tests for pure music-theory logic."""

from pathlib import Path
import sys
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

from guitar_chords_viewer.music_theory import (
    FretPosition,
    VoicingResult,
    calculate_fret_positions,
    calculate_voicing,
    assess_chord_playability,
    get_chord_families,
    get_chord_types,
    get_inversions,
    get_root_notes,
    get_voicing_note,
    validate_music_data,
)


class MusicTheoryTests(unittest.TestCase):
    def test_calculate_voicing_returns_named_result(self):
        voicing = calculate_voicing(
            "Drop 2",
            "Root Position",
            "Major 7 (R-3-5-7)",
            "C",
        )

        self.assertIsInstance(voicing, VoicingResult)
        self.assertEqual(voicing.chord_type, "Drop 2")
        self.assertEqual(voicing.inversion, "Root Position")
        self.assertEqual(voicing.chord_family, "Major 7 (R-3-5-7)")
        self.assertEqual(voicing.root_note, "C")
        self.assertIn(FretPosition(string=4, fret=10, label="R"), voicing.positions)
        self.assertEqual(voicing.frets, {4: 10, 3: 0, 2: 0, 1: 0})
        self.assertEqual(voicing.labels, {4: "R", 3: "5", 2: "7", 1: "3"})

    def test_calculate_c_major_7_drop_2_root_position(self):
        frets, labels = calculate_fret_positions(
            "Drop 2",
            "Root Position",
            "Major 7 (R-3-5-7)",
            "C",
        )

        self.assertEqual(frets, {4: 10, 3: 0, 2: 0, 1: 0})
        self.assertEqual(labels, {4: "R", 3: "5", 2: "7", 1: "3"})

    def test_music_data_validation_passes(self):
        self.assertEqual(validate_music_data(), [])

    def test_supported_four_note_playable_chord_families(self):
        expected = {
            "Major 7 (R-3-5-7)",
            "Minor 7 (R-b3-5-b7)",
            "Dominant 7 (R-3-5-b7)",
            "Major 6 (R-3-5-6)",
            "Minor 6 (R-b3-5-6)",
            "Minor 7 b5 (R-b3-b5-b7)",
            "Diminished 7 (R-b3-b5-bb7)",
            "Minor Major 7 (R-b3-5-7)",
            "Augmented Major 7 (R-3-#5-7)",
            "Augmented Dominant 7 (R-3-#5-b7)",
            "Dominant 7 b5 (R-3-b5-b7)",
            "Dominant 7 #5 (R-3-#5-b7)",
            "Dominant 7 sus4 (R-4-5-b7)",
            "Major 7 #11 shell (R-3-7-#11)",
            "Dominant 9 shell (R-3-b7-9)",
            "Minor 9 shell (R-b3-b7-9)",
            "Major 9 shell (R-3-7-9)",
            "6/9 shell (R-3-6-9)",
            "Minor 6/9 shell (R-b3-6-9)",
            "9sus4 shell (R-4-b7-9)",
            "13 shell (R-3-b7-13)",
            "Minor 11 shell (R-b3-b7-11)",
        }

        self.assertEqual(set(get_chord_families()), expected)

    def test_altered_display_labels_are_shown(self):
        _frets, labels = calculate_fret_positions(
            "Drop 2",
            "Root Position",
            "Minor 7 b5 (R-b3-b5-b7)",
            "C",
        )

        self.assertEqual(labels, {4: "R", 3: "b5", 2: "b7", 1: "b3"})

    def test_voicing_note_is_available(self):
        note = get_voicing_note("Diminished 7 (R-b3-b5-bb7)")

        self.assertIn("diminished", note)

    def test_extended_shell_labels_are_shown(self):
        _frets, labels = calculate_fret_positions(
            "Drop 2",
            "Root Position",
            "13 shell (R-3-b7-13)",
            "C",
        )

        self.assertEqual(labels, {4: "R", 3: "b7", 2: "13", 1: "3"})

    def test_shell_voicing_note_mentions_shell(self):
        note = get_voicing_note("Minor 11 shell (R-b3-b7-11)")

        self.assertIn("Shell", note)

    def test_selected_voicing_has_physical_playability_assessment(self):
        assessment = assess_chord_playability(
            "Drop 2",
            "Root Position",
            "Major 7 (R-3-5-7)",
            "C",
        )

        self.assertIn(assessment.rating, {"playable", "stretchy", "not recommended"})

    def test_selection_lists_are_not_empty(self):
        self.assertGreater(len(get_root_notes()), 0)
        self.assertGreater(len(get_chord_families()), 0)
        self.assertGreater(len(get_chord_types()), 0)
        self.assertGreater(len(get_inversions("Drop 2")), 0)

    def test_caged_shapes_are_supported_voicing_types(self):
        expected_shapes = {
            "CAGED C Shape",
            "CAGED A Shape",
            "CAGED G Shape",
            "CAGED E Shape",
            "CAGED D Shape",
        }

        self.assertTrue(expected_shapes.issubset(set(get_chord_types())))
        self.assertEqual(get_inversions("CAGED C Shape"), ["Standard Shape"])

    def test_caged_shapes_use_caged_chord_qualities(self):
        self.assertEqual(
            get_chord_families("CAGED C Shape"),
            [
                "Major triad (R-3-5)",
                "Minor triad (R-b3-5)",
                "Dominant 7 (R-3-5-b7)",
                "Major 7 (R-3-5-7)",
                "Minor 7 (R-b3-5-b7)",
                "Major 6 (R-3-5-6)",
                "Minor 6 (R-b3-5-6)",
                "Suspended 2 (R-2-5)",
                "Suspended 4 (R-4-5)",
                "Add 9 (R-3-5-9)",
                "Diminished triad (R-b3-b5)",
                "Augmented triad (R-3-#5)",
            ],
        )

    def test_calculate_c_major_caged_c_shape(self):
        frets, labels = calculate_fret_positions(
            "CAGED C Shape",
            "Standard Shape",
            "Major triad (R-3-5)",
            "C",
        )

        self.assertEqual(frets, {5: 3, 4: 2, 3: 0, 2: 1, 1: 0})
        self.assertEqual(labels, {5: "R", 4: "3", 3: "5", 2: "R", 1: "3"})

    def test_calculate_c_major_caged_a_shape(self):
        frets, labels = calculate_fret_positions(
            "CAGED A Shape",
            "Standard Shape",
            "Major triad (R-3-5)",
            "C",
        )

        self.assertEqual(frets, {5: 3, 4: 5, 3: 5, 2: 5, 1: 3})
        self.assertEqual(labels, {5: "R", 4: "5", 3: "R", 2: "3", 1: "5"})

    def test_caged_minor_shape_lowers_thirds(self):
        frets, labels = calculate_fret_positions(
            "CAGED A Shape",
            "Standard Shape",
            "Minor triad (R-b3-5)",
            "C",
        )

        self.assertEqual(frets, {5: 3, 4: 5, 3: 5, 2: 4, 1: 3})
        self.assertEqual(labels, {5: "R", 4: "5", 3: "R", 2: "b3", 1: "5"})

    def test_all_caged_shapes_support_all_caged_chord_families(self):
        for chord_type in get_chord_types():
            if not chord_type.startswith("CAGED"):
                continue

            for chord_family in get_chord_families(chord_type):
                with self.subTest(chord_type=chord_type, chord_family=chord_family):
                    frets, labels = calculate_fret_positions(
                        chord_type,
                        "Standard Shape",
                        chord_family,
                        "C",
                    )

                    self.assertEqual(set(frets), set(labels))
                    self.assertGreaterEqual(len(frets), 3)

    def test_caged_dominant_seventh_labels_are_shown(self):
        _frets, labels = calculate_fret_positions(
            "CAGED E Shape",
            "Standard Shape",
            "Dominant 7 (R-3-5-b7)",
            "E",
        )

        self.assertIn("b7", set(labels.values()))

    def test_caged_suspended_shape_replaces_the_third(self):
        _frets, labels = calculate_fret_positions(
            "CAGED D Shape",
            "Standard Shape",
            "Suspended 4 (R-4-5)",
            "D",
        )

        self.assertIn("4", set(labels.values()))
        self.assertNotIn("3", set(labels.values()))


if __name__ == "__main__":
    unittest.main()
