import time
import random 
import os

def main():
    print('This game is made to ensure the user/player is healthy and not sitting in front of a computer all day')
    while True:
        os.system('cls')
        print('Today you will be given two choices, NIM GAME/RUSSIAN ROULETTE')
        ask_game = input('What game would you like to play?')
        if ask_game == '':
            os.system('cls')
            print('Please enter a valid input')
            time.sleep(0.5)
            perms = False
        elif ask_game == 'nim' or ask_game == 'NIM' or ask_game == 'nim game' or ask_game == 'NIM GAME':
            while True:
                print('You have chosen the NIM game')
                print('Is this correct?')
                confirm = input('(Y/N) ')
                if confirm == '':
                    print('Please enter a valid input')
                    time.sleep(0.5)
                    os.system('cls')
                if confirm == 'y' or confirm == 'Y':
                    confirm = True
                    ask_game = 'NIM'
                    perms = True
                    break
                elif confirm == 'n' or confirm == 'N':
                    print('very well')
                    confirm = False
                    perms = False
                    break
                else:
                    print('Please enter a valid input')
                    time.sleep(0.5)
                    os.system('cls')        
        elif ask_game == 'russian' or ask_game == 'roulette' or ask_game == 'russian roulette':
            while True:
                print('You have chosen Russian Roulette')
                print('Is this correct?')
                confirm = input('(Y/N) ')
                if confirm == '':
                    print('Please enter a valid input')
                    time.sleep(0.5)
                    os.system('cls')
                if confirm == 'y' or confirm == 'Y':
                    confirm = True
                    ask_game = 'roulette'
                    perms = True
                    break
                elif confirm == 'n' or confirm == 'N':
                    print('very well')
                    confirm = False
                    perms = False
                    break
                else:
                    print('Please enter a valid input')
                    time.sleep(0.5)
                    os.system('cls')
        else:
            os.system('cls')
            print('Please choose one of the options provided')
            time.sleep(1)
            perms = False

        if perms == True:    
            if confirm == True and ask_game == 'NIM':
                os.system('cls')
                print('here')
                break


main()