from compute_pda import main

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
    
if __name__ == "__main__":
    welcome()
    main()