"""Guitar playability rules for generated chord voicings."""

from dataclasses import dataclass


EASY = "playable"
STRETCHY = "stretchy"
NOT_RECOMMENDED = "not recommended"

MAX_NOTES_IN_DROP_MODEL = 4
MAX_NOTES_IN_CAGED_MODEL = 6
EASY_MAX_FRET_SPAN = 3
STRETCHY_MAX_FRET_SPAN = 5
MAX_RECOMMENDED_FRET = 18
MAX_OPEN_STRING_FRETTED_POSITION = 5
OPEN_FRET = 0


@dataclass(frozen=True)
class PlayabilityAssessment:
    """Physical playability result for one generated guitar voicing."""

    rating: str
    fret_span: int
    fretted_note_count: int
    message: str


def assess_playability(frets, voicing_note, max_note_count=MAX_NOTES_IN_DROP_MODEL):
    """Classify a generated voicing as playable, stretchy, or not recommended."""
    del voicing_note
    fretted_positions = [fret for fret in frets.values() if fret > OPEN_FRET]
    fret_span = _fret_span(fretted_positions)
    fretted_note_count = len(fretted_positions)

    if len(frets) > max_note_count:
        return PlayabilityAssessment(
            rating=NOT_RECOMMENDED,
            fret_span=fret_span,
            fretted_note_count=fretted_note_count,
            message=f"Not recommended: this voicing uses more than {max_note_count} sounded strings.",
        )

    if fretted_positions and max(fretted_positions) > MAX_RECOMMENDED_FRET:
        return PlayabilityAssessment(
            rating=NOT_RECOMMENDED,
            fret_span=fret_span,
            fretted_note_count=fretted_note_count,
            message=f"Not recommended: highest fret is above {MAX_RECOMMENDED_FRET}.",
        )

    if _mixes_open_strings_with_high_position(frets, fretted_positions):
        return PlayabilityAssessment(
            rating=NOT_RECOMMENDED,
            fret_span=fret_span,
            fretted_note_count=fretted_note_count,
            message="Not recommended: open strings mixed with a high-position fretted note.",
        )

    if fret_span <= EASY_MAX_FRET_SPAN:
        return PlayabilityAssessment(
            rating=EASY,
            fret_span=fret_span,
            fretted_note_count=fretted_note_count,
            message=f"Playable: fret span {fret_span}.",
        )

    if fret_span <= STRETCHY_MAX_FRET_SPAN:
        return PlayabilityAssessment(
            rating=STRETCHY,
            fret_span=fret_span,
            fretted_note_count=fretted_note_count,
            message=f"Stretchy: fret span {fret_span}.",
        )

    return PlayabilityAssessment(
        rating=NOT_RECOMMENDED,
        fret_span=fret_span,
        fretted_note_count=fretted_note_count,
        message=f"Not recommended: fret span {fret_span}.",
    )


def _fret_span(fretted_positions):
    if not fretted_positions:
        return 0
    return max(fretted_positions) - min(fretted_positions)


def _mixes_open_strings_with_high_position(frets, fretted_positions):
    return (
        any(fret == OPEN_FRET for fret in frets.values())
        and bool(fretted_positions)
        and max(fretted_positions) > MAX_OPEN_STRING_FRETTED_POSITION
    )
