"""Audio synthesis and playback for generated guitar chord voicings."""

import math
import platform
import shutil
import struct
import subprocess
import tempfile
import threading
import wave
from pathlib import Path


PLAY_MODE_CHORD = "Chord"
PLAY_MODE_ARPEGGIO = "Arpeggio"
PLAY_MODES = [PLAY_MODE_CHORD, PLAY_MODE_ARPEGGIO]

STRING_OPEN_MIDI = {1: 64, 2: 59, 3: 55, 4: 50, 5: 45, 6: 40}
A4_MIDI_NOTE = 69
A4_FREQUENCY = 440.0
SEMITONES_PER_OCTAVE = 12

SAMPLE_RATE = 44100
SAMPLE_WIDTH_BYTES = 2
CHANNEL_COUNT = 1
CHORD_DURATION_SECONDS = 1.8
ARPEGGIO_NOTE_DELAY_SECONDS = 0.18
ARPEGGIO_TAIL_SECONDS = 1.15
AMPLITUDE = 0.55
CLEAN_HEADROOM = 0.82
ATTACK_SECONDS = 0.006
DECAY_RATE = 2.0
PLUCK_BRIGHTNESS_DECAY_RATE = 8.0
PICK_CLICK_DURATION_SECONDS = 0.012
PICK_CLICK_LEVEL = 0.14
OVERTONE_WEIGHTS = [
    (1, 1.0),
    (2, 0.46),
    (3, 0.24),
    (4, 0.12),
    (5, 0.06),
]
STRING_DETUNE_CENTS = {
    1: 1.5,
    2: -1.0,
    3: 0.8,
    4: -0.7,
    5: 0.4,
    6: -0.5,
}
CENTS_PER_OCTAVE = 1200

TEMP_FILE_SUFFIX = ".wav"
PLAYER_AFPLAY = "afplay"
PLAYER_APLAY = "aplay"
PLAYER_PAPLAY = "paplay"


def midi_note_for_position(string, fret):
    """Return the MIDI note for a guitar string and fret."""
    return STRING_OPEN_MIDI[string] + fret


def frequency_for_midi_note(midi_note):
    """Return frequency in hertz for a MIDI note number."""
    octave_distance = (midi_note - A4_MIDI_NOTE) / SEMITONES_PER_OCTAVE
    return A4_FREQUENCY * (2 ** octave_distance)


def frequencies_for_frets(frets):
    """Return sorted note frequencies for string-to-fret mappings."""
    notes = notes_for_frets(frets)
    return [frequency for _string, _midi_note, frequency in notes]


def notes_for_frets(frets):
    """Return sorted string, MIDI note, and frequency tuples for fretted notes."""
    notes = []
    for string, fret in frets.items():
        midi_note = midi_note_for_position(string, fret)
        frequency = _detuned_frequency(midi_note, string)
        notes.append((string, midi_note, frequency))
    return sorted(notes, key=lambda note: note[1])


def write_chord_wav(frequencies, path, play_mode=PLAY_MODE_CHORD):
    """Write a clean electric-guitar style chord or arpeggio to a WAV file."""
    note_events = _note_events(frequencies, play_mode)
    duration = _render_duration(note_events)
    frame_count = int(SAMPLE_RATE * duration)
    peak_sample = (2 ** ((SAMPLE_WIDTH_BYTES * 8) - 1)) - 1

    with wave.open(str(path), "wb") as wav_file:
        wav_file.setnchannels(CHANNEL_COUNT)
        wav_file.setsampwidth(SAMPLE_WIDTH_BYTES)
        wav_file.setframerate(SAMPLE_RATE)

        for frame in range(frame_count):
            time = frame / SAMPLE_RATE
            sample = sum(_clean_guitar_note_sample(frequency, time - start_time) for frequency, start_time in note_events)
            sample = sample / max(len(note_events), 1)
            sample = math.tanh(sample * AMPLITUDE) * CLEAN_HEADROOM
            sample_value = int(peak_sample * sample)
            wav_file.writeframes(struct.pack("<h", sample_value))


def play_frets(frets, play_mode=PLAY_MODE_CHORD):
    """Generate and play a chord asynchronously. Return True if playback starts."""
    player = _audio_player_command()
    if player is None:
        return False

    frequencies = frequencies_for_frets(frets)
    temp_file = tempfile.NamedTemporaryFile(suffix=TEMP_FILE_SUFFIX, delete=False)
    temp_path = Path(temp_file.name)
    temp_file.close()
    write_chord_wav(frequencies, temp_path, play_mode=play_mode)

    thread = threading.Thread(target=_play_and_cleanup, args=(player, temp_path), daemon=True)
    thread.start()
    return True


def _note_events(frequencies, play_mode):
    if play_mode == PLAY_MODE_ARPEGGIO:
        return [(frequency, index * ARPEGGIO_NOTE_DELAY_SECONDS) for index, frequency in enumerate(frequencies)]
    return [(frequency, 0.0) for frequency in frequencies]


def _render_duration(note_events):
    if not note_events:
        return CHORD_DURATION_SECONDS
    last_start_time = max(start_time for _frequency, start_time in note_events)
    return max(CHORD_DURATION_SECONDS, last_start_time + ARPEGGIO_TAIL_SECONDS)


def _clean_guitar_note_sample(frequency, time):
    if time < 0:
        return 0.0

    envelope = _amplitude_envelope(time)
    brightness = math.exp(-PLUCK_BRIGHTNESS_DECAY_RATE * time)
    sample = 0.0
    for harmonic, weight in OVERTONE_WEIGHTS:
        harmonic_weight = weight * (brightness if harmonic > 1 else 1.0)
        sample += harmonic_weight * math.sin(2 * math.pi * frequency * harmonic * time)

    if time < PICK_CLICK_DURATION_SECONDS:
        sample += PICK_CLICK_LEVEL * (1.0 - time / PICK_CLICK_DURATION_SECONDS) * math.sin(2 * math.pi * frequency * 7 * time)

    return envelope * sample


def _amplitude_envelope(time):
    if time < 0:
        return 0.0
    if time < ATTACK_SECONDS:
        return time / ATTACK_SECONDS
    return math.exp(-DECAY_RATE * (time - ATTACK_SECONDS))


def _detuned_frequency(midi_note, string):
    frequency = frequency_for_midi_note(midi_note)
    cents = STRING_DETUNE_CENTS.get(string, 0.0)
    return frequency * (2 ** (cents / CENTS_PER_OCTAVE))


def _audio_player_command():
    if platform.system() == "Darwin" and shutil.which(PLAYER_AFPLAY):
        return [PLAYER_AFPLAY]
    if shutil.which(PLAYER_APLAY):
        return [PLAYER_APLAY]
    if shutil.which(PLAYER_PAPLAY):
        return [PLAYER_PAPLAY]
    return None


def _play_and_cleanup(player, path):
    try:
        subprocess.run([*player, str(path)], check=False)
    finally:
        path.unlink(missing_ok=True)
