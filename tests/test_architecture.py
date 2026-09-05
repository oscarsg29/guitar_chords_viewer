"""Tests for package architecture boundaries."""

import ast
from pathlib import Path
import sys
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

from guitar_chords_viewer import music_theory


PACKAGE_DIR = SRC_DIR / "guitar_chords_viewer"
DOMAIN_MODULES = {
    "audio.py",
    "fretboard.py",
    "music_theory.py",
    "playability.py",
}
DISALLOWED_DOMAIN_IMPORTS = {
    "tkinter",
    "guitar_chords_viewer.ui_tkinter",
    "guitar_chords_viewer.app",
}


class ArchitectureTests(unittest.TestCase):
    def test_domain_modules_do_not_import_ui_or_app_layers(self):
        for module_name in DOMAIN_MODULES:
            with self.subTest(module=module_name):
                imports = _module_imports(PACKAGE_DIR / module_name)

                self.assertTrue(DISALLOWED_DOMAIN_IMPORTS.isdisjoint(imports))

    def test_ui_layer_does_not_own_music_data(self):
        imports = _module_imports(PACKAGE_DIR / "ui_tkinter.py")

        self.assertIn("tkinter", imports)
        self.assertIn("guitar_chords_viewer.music_theory", imports)

    def test_layout_validation_reports_missing_interval_labels(self):
        errors = music_theory._validate_layout(
            "test layout",
            {4: (0, "missing")},
            {"quality": music_theory.CHORD_QUALITIES["Major 7 (R-3-5-7)"]},
        )

        self.assertTrue(any("missing from" in error for error in errors))

    def test_layout_validation_reports_invalid_frets(self):
        errors = music_theory._validate_layout(
            "test layout",
            {4: (-1, "R")},
            {"quality": music_theory.CHORD_QUALITIES["Major 7 (R-3-5-7)"]},
        )

        self.assertTrue(any("invalid fret" in error for error in errors))


def _module_imports(path):
    imports = set()
    tree = ast.parse(path.read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module)
    return imports


if __name__ == "__main__":
    unittest.main()
