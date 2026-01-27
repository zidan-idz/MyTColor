
import sys
from . import MyT, __version__

def main():
    if len(sys.argv) > 1:
        # Check for version flag
        if sys.argv[1] == '--version' or sys.argv[1] == '-v':
            print(f'MyTColor version {__version__}')
            return
        elif sys.argv[1] == '--help' or sys.argv[1] == '-h':
            print(f'MyTColor v{__version__}')
            print('Usage:')
            print('  python -m MyTColor --version   Show version')
            return

    # Default output
    print(f'{MyT.BOLD}MyTColor v{__version__}{MyT.RESET}')
    print('Run \'python -m MyTColor --help\' for options.')

if __name__ == '__main__':
    main()
