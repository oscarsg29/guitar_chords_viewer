"""Tests for chord audio helpers."""

from pathlib import Path
import sys
import tempfile
import unittest
import wave


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

from guitar_chords_viewer.audio import (
    CHORD_DURATION_SECONDS,
    CHANNEL_COUNT,
    PLAY_MODE_ARPEGGIO,
    PLAY_MODE_CHORD,
    SAMPLE_RATE,
    SAMPLE_WIDTH_BYTES,
    frequencies_for_frets,
    frequency_for_midi_note,
    midi_note_for_position,
    notes_for_frets,
    write_chord_wav,
)


class AudioTests(unittest.TestCase):
    def test_midi_note_for_position_uses_standard_tuning(self):
        self.assertEqual(midi_note_for_position(6, 0), 40)
        self.assertEqual(midi_note_for_position(1, 0), 64)
        self.assertEqual(midi_note_for_position(1, 12), 76)

    def test_a4_frequency(self):
        self.assertEqual(frequency_for_midi_note(69), 440.0)

    def test_frequencies_for_frets_are_sorted_by_pitch(self):
        frequencies = frequencies_for_frets({1: 0, 6: 0})

        self.assertLess(frequencies[0], frequencies[1])

    def test_notes_for_frets_include_string_and_midi_note(self):
        notes = notes_for_frets({1: 0, 6: 0})

        self.assertEqual(notes[0][0], 6)
        self.assertEqual(notes[0][1], 40)
        self.assertEqual(notes[1][0], 1)
        self.assertEqual(notes[1][1], 64)

    def test_write_chord_wav_creates_valid_wave_file(self):
        with tempfile.NamedTemporaryFile(suffix=".wav") as temp_file:
            path = Path(temp_file.name)
            write_chord_wav([220.0, 330.0], path, play_mode=PLAY_MODE_CHORD)

            with wave.open(str(path), "rb") as wav_file:
                self.assertEqual(wav_file.getnchannels(), CHANNEL_COUNT)
                self.assertEqual(wav_file.getsampwidth(), SAMPLE_WIDTH_BYTES)
                self.assertEqual(wav_file.getframerate(), SAMPLE_RATE)
                self.assertGreater(wav_file.getnframes(), 0)

    def test_arpeggio_wav_is_at_least_chord_duration(self):
        with tempfile.NamedTemporaryFile(suffix=".wav") as temp_file:
            path = Path(temp_file.name)
            write_chord_wav([220.0, 330.0, 440.0, 550.0], path, play_mode=PLAY_MODE_ARPEGGIO)

            with wave.open(str(path), "rb") as wav_file:
                self.assertGreaterEqual(wav_file.getnframes(), int(SAMPLE_RATE * CHORD_DURATION_SECONDS))


if __name__ == "__main__":
    unittest.main()
