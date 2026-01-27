
import os
import ctypes

def enable_windows_vt():
    """
    Enables Virtual Terminal Processing on Windows.
    """
    if os.name == 'nt':
        try:
            # Enable VT Processing (0x0004)
            kernel32 = ctypes.windll.kernel32
            handle = kernel32.GetStdHandle(-11) # STD_OUTPUT_HANDLE
            mode = ctypes.c_ulong()
            kernel32.GetConsoleMode(handle, ctypes.byref(mode))
            
            # Check and enable if needed
            if not (mode.value & 0x0004):
                kernel32.SetConsoleMode(handle, mode.value | 0x0004)
        except Exception:
            # Silently fail on error
            pass
