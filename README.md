# MyTColor

[![Author](https://img.shields.io/badge/Author-Zidan%20IDz-%23FF0000?style=for-the-badge&logo=github)](https://github.com/zidan-idz)
[![Version](<https://img.shields.io/badge/Version-1.0.0%20(Haku)-%23FF0000?style=for-the-badge&logo=python>)](https://github.com/zidan-idz)
[![Language](https://img.shields.io/badge/Language-Python-%23FF0000?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-%23FF0000?style=for-the-badge)](LICENSE)

**MyTColor** is a **Simple, Fast, and Efficient** Python library for terminal text coloring.
Designed with zero dependencies and native support for Windows, Linux, and macOS.

---

## 📦 Installation

Easily install via pip:

```bash
pip install MyTColor
```

## 🚀 Usage

Import `MyT` and use it within `print` statements (f-strings recommended).

```python
from MyTColor import MyT

# 1. Standard Colors
print(f'{MyT.RED}This is red text{MyT.RESET}')

# 2. Combinations (Bold + Blue Background + White Text)
print(f'{MyT.BOLD}{MyT.BG_BLUE}{MyT.WHITE}Important Info{MyT.RESET}')
```

## 🎨 Color Reference

Below is the complete list of available commands.

### 1. Text Colors (Foreground)

| Standard    | Code          | Bright (Light)    | Code            |
| :---------- | :------------ | :---------------- | :-------------- |
| **Black**   | `MyT.BLACK`   | **Light Black**   | `MyT.L_BLACK`   |
| **Red**     | `MyT.RED`     | **Light Red**     | `MyT.L_RED`     |
| **Green**   | `MyT.GREEN`   | **Light Green**   | `MyT.L_GREEN`   |
| **Yellow**  | `MyT.YELLOW`  | **Light Yellow**  | `MyT.L_YELLOW`  |
| **Blue**    | `MyT.BLUE`    | **Light Blue**    | `MyT.L_BLUE`    |
| **Magenta** | `MyT.MAGENTA` | **Light Magenta** | `MyT.L_MAGENTA` |
| **Cyan**    | `MyT.CYAN`    | **Light Cyan**    | `MyT.L_CYAN`    |
| **White**   | `MyT.WHITE`   | **Light White**   | `MyT.L_WHITE`   |

### 2. Background Colors

Use the `BG_` prefix (e.g., `MyT.BG_RED`). Available for all standard and bright colors listed above.

### 3. Text Styles

- `MyT.BOLD` : **Bold**
- `MyT.DIM` : Dim
- `MyT.ITALIC` : _Italic_
- `MyT.UNDERLINE` : Underline
- `MyT.BLINK` : Blink
- `MyT.REVERSE` : Reverse (Swap Background <-> Foreground)
- `MyT.HIDDEN` : Hidden
- `MyT.STRIKETHROUGH` : Strikethrough

### 4. Reset

Always reset at the end of your string!

- `MyT.RESET` or `MyT.R`

---

## � Changelog

See full history in [CHANGELOG.md](CHANGELOG.md).

**Latest: v1.0.0 "Haku"**

- Initial Release.
- 32 Colors, Windows VT Support, Modular Architecture.

## �📄 License

Distributed under the **MIT** License.
Free for personal and commercial use.
