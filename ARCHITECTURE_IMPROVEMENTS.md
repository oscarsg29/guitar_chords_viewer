# Architecture Improvements Roadmap

This file tracks possible architecture and design improvements that are not required for the app to run today.

Priority scale:

- High: improves correctness, maintainability, or future feature work soon.
- Medium: useful after the core model is more stable.
- Low: valuable only if the app grows or the current approach becomes painful.

## Recommended Improvements

| Priority | Improvement | Intention |
| --- | --- | --- |
| High | Add explicit domain model objects | Replace parallel dictionaries with named results such as `VoicingResult`, `FretPosition`, or `SelectedVoicing` so code is easier to read and extend. |
| High | Add shape data validation | Verify every chord layout interval exists in its chord quality, every generated fret is non-negative, and fret/label keys match. |
| High | Define module boundary rules | Make allowed imports explicit so UI, music theory, playability, drawing, and audio responsibilities stay separated. |
| High | Expand testing strategy | Document which tests belong to music theory, playability, audio, UI helpers, and optional GUI smoke checks. |
| Medium | Split large music data | Move Drop and CAGED shape data into separate modules if `music_theory.py` becomes hard to scan. |
| Medium | Add error handling strategy | Define how invalid selections, unsupported audio playback, and missing system players should be reported. |
| Medium | Document data ownership | Make chord formulas, CAGED layouts, Drop shapes, tuning data, and UI labels clearly owned by the domain layer. |
| Medium | Add extension workflow | Provide a short checklist for adding chord families, shapes, tests, docs, and verification. |
| Low | Add configuration strategy | Decide which constants should later become user settings, such as tuning, audio tone, window behavior, and colors. |
| Low | Add dependency policy | Keep the standard-library-first approach and document when a new dependency is worth adding. |

## Suggested Order

1. Add shape data validation.
2. Introduce a `VoicingResult` dataclass.
3. Document module boundary rules.
4. Expand testing strategy.
5. Add extension workflow.
6. Split Drop and CAGED data if `music_theory.py` keeps growing.
7. Add error handling strategy.
8. Document data ownership in more detail.
9. Add configuration strategy.
10. Add dependency policy.

## Source-Of-Truth Notes

- Current architecture rules belong in `DESIGN_PRINCIPLES.md`.
- Current architecture compliance belongs in `DESIGN_PRINCIPLES_CHECKLIST.md`.
- Current file responsibilities belong in `PROJECT_STRUCTURE.md`.
- This file only tracks future improvements and their priority.
