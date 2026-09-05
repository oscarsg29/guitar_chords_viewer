"""Guitar playability rules for generated chord voicings."""

from dataclasses import dataclass


EASY = "playable"
STRETCHY = "stretchy"
NOT_RECOMMENDED = "not recommended"

MAX_NOTES_IN_CURRENT_MODEL = 4
EASY_MAX_FRET_SPAN = 3
STRETCHY_MAX_FRET_SPAN = 5
MAX_RECOMMENDED_FRET = 18
OPEN_FRET = 0


@dataclass(frozen=True)
class PlayabilityAssessment:
    """Physical playability result for one generated guitar voicing."""

    rating: str
    fret_span: int
    fretted_note_count: int
    message: str


def assess_playability(frets, voicing_note):
    """Classify a generated voicing as playable, stretchy, or not recommended."""
    fretted_positions = [fret for fret in frets.values() if fret > OPEN_FRET]
    fret_span = _fret_span(fretted_positions)
    fretted_note_count = len(fretted_positions)

    if len(frets) > MAX_NOTES_IN_CURRENT_MODEL:
        return PlayabilityAssessment(
            rating=NOT_RECOMMENDED,
            fret_span=fret_span,
            fretted_note_count=fretted_note_count,
            message="Not recommended: this app currently supports four-note grips.",
        )

    if fretted_positions and max(fretted_positions) > MAX_RECOMMENDED_FRET:
        return PlayabilityAssessment(
            rating=NOT_RECOMMENDED,
            fret_span=fret_span,
            fretted_note_count=fretted_note_count,
            message=f"Not recommended: highest fret is above {MAX_RECOMMENDED_FRET}. {voicing_note}",
        )

    if fret_span <= EASY_MAX_FRET_SPAN:
        return PlayabilityAssessment(
            rating=EASY,
            fret_span=fret_span,
            fretted_note_count=fretted_note_count,
            message=f"Playable: fret span {fret_span}. {voicing_note}",
        )

    if fret_span <= STRETCHY_MAX_FRET_SPAN:
        return PlayabilityAssessment(
            rating=STRETCHY,
            fret_span=fret_span,
            fretted_note_count=fretted_note_count,
            message=f"Stretchy: fret span {fret_span}. {voicing_note}",
        )

    return PlayabilityAssessment(
        rating=NOT_RECOMMENDED,
        fret_span=fret_span,
        fretted_note_count=fretted_note_count,
        message=f"Not recommended: fret span {fret_span}. {voicing_note}",
    )


def _fret_span(fretted_positions):
    if not fretted_positions:
        return 0
    return max(fretted_positions) - min(fretted_positions)
