import argparse
from lexer import*

def welcome():
    print("\033c", end="")
    print('''
                                   Welcome To 
 _   _ ________  ___ _       _____  _   _  _____ _____  _   __ ___________ 
| | | |_   _|  \/  || |     /  __ \| | | ||  ___/  __ \| | / /|  ___| ___ |
| |_| | | | | .  . || |     | /  \/| |_| || |__ | /  \/| |/ / | |__ | |_/ /
|  _  | | | | |\/| || |     | |    |  _  ||  __|| |    |    \ |  __||    / 
| | | | | | | |  | || |____ | \__/\| | | || |___| \__/\| |\  \| |___| |\ \ 
\_| |_/ \_/ \_|  |_/\_____/  \____/\_| |_/\____/ \____/\_| \_/\____/\_| \_|
                                                                                                           
        ''')

def verdict():
    pda_path = "pda/"
    html_path = "html/"

    arg = argparse.ArgumentParser()
    arg.add_argument('pda', type=str, default=pda_path)
    arg.add_argument('html', type=str, default=html_path)
    
    args = arg.parse_args()

    welcome()
    print("File name: " + str(args.html))
    print()
    checkhtml(args.html)
    
if __name__ == "__main__":
    verdict()
