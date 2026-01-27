# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2026-01-27 "Haku"

### Added

- **Core**: 32 ANSI Colors (Standard & Bright) for Foreground and Background.
- **Styles**: Bold, Dim, Italic, Underline, Blink, Reverse, Hidden, Strikethrough.
- **Cross-Platform**: Automatic Windows VT processing support via `ctypes`.
- **CLI**: Version check command `python -m MyTColor --version`.
- **Modular Architecture**: Split into `colors.py` and `utils.py` for future extensibility.
- **Zero-Dependency**: Pure Python implementation.
