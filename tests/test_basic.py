
import unittest
import sys
import os

# Insert parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from MyTColor import MyT

class TestMyTColor(unittest.TestCase):
    
    def test_basic_colors(self):
        """Test that basic color constants are correct ANSI strings."""
        self.assertEqual(MyT.RED, '\033[31m')
        self.assertEqual(MyT.GREEN, '\033[32m')
        self.assertEqual(MyT.BLUE, '\033[34m')
        self.assertEqual(MyT.RESET, '\033[0m')
        
    def test_styles(self):
        """Test style constants."""
        self.assertEqual(MyT.BOLD, '\033[1m')
        
        # Verify invalid access raises AttributeError
        with self.assertRaises(AttributeError):
            _ = MyT.DATA_STYLES
        
    def test_backgrounds(self):
        """Test background constants."""
        self.assertEqual(MyT.BG_RED, '\033[41m')
        self.assertEqual(MyT.BG_WHITE, '\033[47m')
        
    def test_bright_colors(self):
        """Test bright/light color constants."""
        self.assertEqual(MyT.L_RED, '\033[91m')
        self.assertEqual(MyT.BG_L_BLUE, '\033[104m')

    def test_aliasing(self):
        """Test that class aliasing works as expected."""
        Color = MyT
        self.assertEqual(Color.RED, MyT.RED)

if __name__ == '__main__':
    unittest.main()
