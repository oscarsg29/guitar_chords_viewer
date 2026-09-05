# Architecture Improvements Roadmap

This file tracks possible architecture and design improvements that are not required for the app to run today.

Priority scale:

- High: improves correctness, maintainability, or future feature work soon.
- Medium: useful after the core model is more stable.
- Low: valuable only if the app grows or the current approach becomes painful.

## Completed Improvements

| Priority | Improvement | Current State |
| --- | --- | --- |
| High | Add explicit domain model objects | `calculate_voicing()` returns `VoicingResult` values composed of `FretPosition` objects. |
| High | Add shape data validation | Import-time validation checks chord qualities, Drop layouts, CAGED layouts, and generated voicing output. |
| High | Define module boundary rules | Architecture tests guard domain modules against UI and app-layer imports. |
| High | Expand testing strategy | Tests now cover architecture boundaries and shape-data validation in addition to music theory, playability, audio, fretboard helpers, and UI helpers. |

## Recommended Improvements

| Priority | Improvement | Intention |
| --- | --- | --- |
| Medium | Split large music data | Move Drop and CAGED shape data into separate modules if `music_theory.py` becomes hard to scan. |
| Medium | Add error handling strategy | Define how invalid selections, unsupported audio playback, and missing system players should be reported. |
| Medium | Document data ownership | Make chord formulas, CAGED layouts, Drop shapes, tuning data, and UI labels clearly owned by the domain layer. |
| Medium | Add extension workflow | Provide a short checklist for adding chord families, shapes, tests, docs, and verification. |
| Low | Add configuration strategy | Decide which constants should later become user settings, such as tuning, audio tone, window behavior, and colors. |
| Low | Add dependency policy | Keep the standard-library-first approach and document when a new dependency is worth adding. |

## Suggested Order

1. Add extension workflow.
2. Split Drop and CAGED data if `music_theory.py` keeps growing.
3. Add error handling strategy.
4. Document data ownership in more detail.
5. Add configuration strategy.
6. Add dependency policy.

## Source-Of-Truth Notes

- Current architecture rules belong in `DESIGN_PRINCIPLES.md`.
- Current architecture compliance belongs in `DESIGN_PRINCIPLES_CHECKLIST.md`.
- Current file responsibilities belong in `PROJECT_STRUCTURE.md`.
- This file only tracks future improvements and their priority.
