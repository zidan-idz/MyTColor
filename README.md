# MyTColor

[![Version](https://img.shields.io/badge/version-1.0.1-blue?style=flat&logo=pypi)](https://pypi.org/project/MyTColor/)
[![Python](https://img.shields.io/badge/python-3.6+-blue?style=flat&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat)](LICENSE)

**MyTColor** provides a lightweight, dependency-free interface for ANSI terminal formatting in Python. It offers a straightforward API for adding colors and styles to terminal output, suitable for logging, CUI (Console User Interface) development, and script enhancements.

Key features:

- **Zero Dependencies**: Pure Python implementation using standard libraries.
- **Cross-Platform**: Native support for ANSI sequences on Linux, macOS, and automatic Virtual Terminal processing on Windows.
- **Performance**: Uses static string constants for minimal runtime overhead.
- **Type Safety**: Compatible with standard Python type checking.

## Installation

Install via pip:

```bash
pip install MyTColor
```

## Usage

MyTColor exposes ANSI sequences as string constants through the `MyT` class. This design allows for seamless integration with Python's f-strings.

### Basic Example

```python
from MyTColor import MyT

# Success message
print(f"{MyT.GREEN}✔ Operation completed successfully.{MyT.RESET}")

# Error message with style
print(f"{MyT.RED}{MyT.BOLD}✖ Error: Connection failed.{MyT.RESET}")
```

### Advanced Formatting

Combine background colors, styles, and foreground colors for rich output.

```python
# Header style: Bold white text on blue background
header_style = f"{MyT.BOLD}{MyT.BG_BLUE}{MyT.WHITE}"
print(f"{header_style} SYSTEM STATUS {MyT.RESET}")
```

## API Reference

The `MyT` class provides the following constants.

### Foreground Colors

| Standard | Accessor      | Bright  | Accessor        |
| -------- | ------------- | ------- | --------------- |
| Black    | `MyT.BLACK`   | Black   | `MyT.L_BLACK`   |
| Red      | `MyT.RED`     | Red     | `MyT.L_RED`     |
| Green    | `MyT.GREEN`   | Green   | `MyT.L_GREEN`   |
| Yellow   | `MyT.YELLOW`  | Yellow  | `MyT.L_YELLOW`  |
| Blue     | `MyT.BLUE`    | Blue    | `MyT.L_BLUE`    |
| Magenta  | `MyT.MAGENTA` | Magenta | `MyT.L_MAGENTA` |
| Cyan     | `MyT.CYAN`    | Cyan    | `MyT.L_CYAN`    |
| White    | `MyT.WHITE`   | White   | `MyT.L_WHITE`   |

### Background Colors

Prefix any color with `BG_`.

- Example: `MyT.BG_RED`, `MyT.BG_L_BLUE`.

### Styles

- `MyT.BOLD`: **Bold**
- `MyT.DIM`: Dim/Faint
- `MyT.ITALIC`: _Italic_
- `MyT.UNDERLINE`: <u>Underline</u>
- `MyT.BLINK`: Blink
- `MyT.REVERSE`: Invert colors
- `MyT.HIDDEN`: Hidden text
- `MyT.STRIKETHROUGH`: Strikethrough

### Utilities

- `MyT.RESET`: Resets all formatting. Essential to prevent style leakage.

## Compatibility

MyTColor automatically enables standard ANSI support on Windows 10 and 11 terminals using `ctypes`. On Unix-like systems (Linux, macOS), it outputs standard ANSI sequences directly.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
