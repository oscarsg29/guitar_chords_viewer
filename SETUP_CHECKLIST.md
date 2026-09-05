# Setup Checklist

Use this checklist to make `guitarChordsViewer.py` run locally as a native Python desktop script.

## Required System Pieces

- [x] Python 3 is installed.
- [x] `tkinter` is available in the Python standard library:

```bash
python3 -c 'import tkinter; print(tkinter.TkVersion)'
```

- [x] The script passes Python syntax compilation:

```bash
python3 -m py_compile guitarChordsViewer.py src/guitar_chords_viewer/*.py tests/test_music_theory.py
```

- [x] The unit tests pass:

```bash
python3 -m unittest discover -s tests
```

- [x] The desktop window can be created and closed by a smoke test:

```bash
python3 -c 'import sys; sys.path.insert(0, "src"); from guitar_chords_viewer.ui_tkinter import GuitarChordViewer; app = GuitarChordViewer(); app.update(); print(app.title()); app.destroy()'
```

## Run The App

- [x] Start the native Python app from the project directory:

```bash
python3 guitarChordsViewer.py
```

- [x] Confirm the desktop window opens.

## Current Repository Gaps

- [x] Remove third-party web app dependencies.
- [x] Remove the Streamlit web server requirement.
- [ ] Optionally add a virtual environment workflow.
- [x] Add executable permissions for direct script execution.

## Known Runtime Notes

- This is a native Python desktop app.
- The app uses `tkinter` from the Python standard library for the desktop UI.
- `guitarChordsViewer.py` is a small launcher that calls `src/guitar_chords_viewer/app.py`.
- It can also be launched directly with `./guitarChordsViewer.py`.
- The script passes Python syntax compilation.
- Verified `tkinter` version: 8.6.
