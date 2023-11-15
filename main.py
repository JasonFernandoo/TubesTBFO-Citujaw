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
    arg = argparse.ArgumentParser()
    arg.add_argument('file', type = argparse.FileType('r'))
    args = arg.parse_args()

    welcome()
    print("File name: " + str(args.file.name))
    print()
    createToken(args.file.name)
    
if __name__ == "__main__":
    verdict()