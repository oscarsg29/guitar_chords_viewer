#!/usr/bin/env python3
"""Compatibility launcher for the native Python guitar chord viewer."""

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parent
SRC_DIR = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

from guitar_chords_viewer.app import main


if __name__ == "__main__":
    main()
