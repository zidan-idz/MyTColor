
from MyTColor import MyT
import time

def demo():
    print(f'\n{MyT.BOLD}{MyT.UNDERLINE}MyTColor Featured Demo{MyT.RESET}\n')

    print('1. Standard Colors:')
    print(f'  {MyT.RED}RED{MyT.RESET} {MyT.GREEN}GREEN{MyT.RESET} {MyT.YELLOW}YELLOW{MyT.RESET} {MyT.BLUE}BLUE{MyT.RESET} {MyT.MAGENTA}MAGENTA{MyT.RESET} {MyT.CYAN}CYAN{MyT.RESET} {MyT.WHITE}WHITE{MyT.RESET}')

    print('\n2. Bright/Light Colors (L_...):')
    print(f'  {MyT.L_RED}L_RED{MyT.RESET} {MyT.L_GREEN}L_GREEN{MyT.RESET} {MyT.L_YELLOW}L_YELLOW{MyT.RESET} {MyT.L_BLUE}L_BLUE{MyT.RESET} {MyT.L_MAGENTA}L_MAGENTA{MyT.RESET} {MyT.L_CYAN}L_CYAN{MyT.RESET}')

    print('\n3. Backgrounds (BG_...):')
    print(f'  {MyT.BG_RED}{MyT.WHITE} RED BG {MyT.RESET} {MyT.BG_GREEN}{MyT.BLACK} GREEN BG {MyT.RESET} {MyT.BG_BLUE}{MyT.L_WHITE} BLUE BG {MyT.RESET}')

    print('\n4. Styles:')
    print(f'  {MyT.BOLD}BOLD{MyT.RESET} {MyT.DIM}DIM{MyT.RESET} {MyT.ITALIC}ITALIC{MyT.RESET} {MyT.REVERSE}REVERSE{MyT.RESET}')

    print('\n5. Combining (Mix & Match):')
    print(f'  {MyT.BOLD}{MyT.L_WHITE}{MyT.BG_RED} BOLD WHITE ON RED {MyT.RESET}')

    print('\n6. Aliasing Test (import as \'Color\'):')
    # Simulate alias usage
    Color = MyT
    print(f'  {Color.CYAN}Hello from \'Color\' alias!{Color.RESET}')

if __name__ == '__main__':
    demo()
