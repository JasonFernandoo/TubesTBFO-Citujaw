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
    path = "html\\"

    welcome()
    file = input("Input File: ")
    path += file
    try:
        with open(path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"The file at {path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    print()
    createToken(path)
    
if __name__ == "__main__":
    verdict()