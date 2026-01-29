
from .colors import *
from .utils import enable_windows_vt

__version__ = '1.0.1'

class MyT:
    """
    MyTColor: Simple, fast, zero-dependency terminal coloring.
    """
    
    # Auto-enable Windows support
    enable_windows_vt()

    # Define Colors (Standard)
    BLACK = BLACK
    RED = RED
    GREEN = GREEN
    YELLOW = YELLOW
    BLUE = BLUE
    MAGENTA = MAGENTA
    CYAN = CYAN
    WHITE = WHITE
    
    # Define Colors (Bright)
    L_BLACK = L_BLACK
    L_RED = L_RED
    L_GREEN = L_GREEN
    L_YELLOW = L_YELLOW
    L_BLUE = L_BLUE
    L_MAGENTA = L_MAGENTA
    L_CYAN = L_CYAN
    L_WHITE = L_WHITE
    
    # Define Backgrounds (Standard)
    BG_BLACK = BG_BLACK
    BG_RED = BG_RED
    BG_GREEN = BG_GREEN
    BG_YELLOW = BG_YELLOW
    BG_BLUE = BG_BLUE
    BG_MAGENTA = BG_MAGENTA
    BG_CYAN = BG_CYAN
    BG_WHITE = BG_WHITE
    
    # Define Backgrounds (Bright)
    BG_L_BLACK = BG_L_BLACK
    BG_L_RED = BG_L_RED
    BG_L_GREEN = BG_L_GREEN
    BG_L_YELLOW = BG_L_YELLOW
    BG_L_BLUE = BG_L_BLUE
    BG_L_MAGENTA = BG_L_MAGENTA
    BG_L_CYAN = BG_L_CYAN
    BG_L_WHITE = BG_L_WHITE

    # Define Styles
    RESET = RESET
    R = RESET
    BOLD = BOLD
    DIM = DIM
    ITALIC = ITALIC
    UNDERLINE = UNDERLINE
    BLINK = BLINK
    RAPID_BLINK = RAPID_BLINK
    REVERSE = REVERSE
    HIDDEN = HIDDEN
    STRIKETHROUGH = STRIKETHROUGH
