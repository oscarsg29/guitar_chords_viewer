"""Application entry point."""

from guitar_chords_viewer.ui_tkinter import GuitarChordViewer


def main():
    app = GuitarChordViewer()
    app.mainloop()


if __name__ == "__main__":
    main()
