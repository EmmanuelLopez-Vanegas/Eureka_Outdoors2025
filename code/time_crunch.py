import time
import random 
import os


def choose_game():
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
                break
            if confirm == True and ask_game == 'roulette':
                os.system('cls')
                break

    return ask_game

def selectpileandcounters(piles):
    control = False
    while control == False:
        askPiles = input('What pile would you like to remove counters from (1/2/3)? ')
        if askPiles == '1' or askPiles == '2' or askPiles == '3':
            if piles[int(askPiles)-1] == 0:
                print('This Pile is empty, please select another Pile')
            else:
                control = True
        else:
            print('Please enter a valid Input from 1-3')
    control = False
    while control == False:
        askCounter = input(f'How many counters would you like to remove from Pile {askPiles}? ')
        if askCounter.isdigit():
            askCounters = int(askCounter)
            if int(askCounters) > piles[int(askPiles)-1]:
                print(f'Number exceeds amount of counters in Pile {askPiles}, current amount of counters is {piles[int(askPiles)-1]}')
            elif askCounters <= 0:
                print(f'Must Select at least one counter from Pile {askPiles}')
            else:
                piles[int(askPiles)-1] = piles[int(askPiles)-1] - askCounters
                control = True
        else:
            print(f'Please enter a valid number beetween 1 and {piles[int(askPiles)-1]}')
    return piles

def xor(piles):
    temp0 = piles[0]
    temp1 = piles[1]
    temp2 = piles[2]
    xor = 0
    temp = [temp0, temp1, temp2]
    pos = temp.index(max(temp))
    condition = sum(temp)
    while xor != 1:
        if condition > 1:
            temp[pos] = temp[pos] -1
            condition = condition -1
            xor = temp[0] ^ temp[1] ^ temp[2]
        else:
            xor = 1
            temp[pos] = 0
    return temp

def print_piles(piles, name, round):
    os.system('cls')
    print(f"Round {round}")
    print('\n')
    print('Pile 1 has',piles[0],'Counters: ','* '*piles[0])
    print('Pile 2 has',piles[1],'Counters: ','* '*piles[1])
    print('Pile 3 has',piles[2],'Counters: ','* '*piles[2])
    print('\n')
    print('It is',name,"'s Turn")

def game_rendering(names):
    print('LOCAL GAME BEING RENDERED')
    time.sleep(0.5)
    for i in range(5, 0, -1):
        os.system('cls')
        print(f'Game Loading... for {names[0]} and {names[1]}  ', i)
        print(f'Piles are being calculated...')
        time.sleep(0.5)
    time.sleep(0.5)
    return

def pile_random_gen():
    os.system('cls')
    print("Let's Begin")
    piles = [0,0,0]
    counters = random.randint(3,100)
    piles[0] = random.randint(1,counters - 2)
    piles[1] = random.randint(1,counters - piles[0] - 1)
    piles[2] = counters - piles[0] - piles[1]
    return piles

def playing(piles, names):
    keepPlaying = True
    round = 0
    winner = ''
    loser = ''
    while keepPlaying == True:
        round = round + 1
        for name in names: 
            print_piles(piles, name, round)
            time.sleep(1)
            if name != 'CPU':
                piles = selectpileandcounters(piles)
            else:
                piles = xor(piles)
            totalCounters = piles[0] + piles[1] + piles[2]
            if totalCounters == 1:
                winner = name
                keepPlaying = False
                break
            elif totalCounters == 0:
                loser = name
                keepPlaying = False
                break             
    return loser, winner, piles

def winningANDlosing(loser, winner, names, piles):
    os.system('cls')
    print('Pile 1 has',piles[0],'Counters: ','* '*piles[0])
    print('Pile 2 has',piles[1],'Counters: ','* '*piles[1])
    print('Pile 3 has',piles[2],'Counters: ','* '*piles[2])
    if loser == names[0]:
        print(f'{loser} has taken the last counter')
        print(f'{names[1]} wins')
    elif loser == names[1]:
        print(f'{loser} has taken the last counter')
        print(f'{names[0]} wins')
    if winner == names[0]:
        print(f'{names[1]} has been forced to take the last counter')
        print(f'{winner} wins')
    elif winner == names[1]:
        print(f'{names[0]} has been forced to take the last counter')
        print(f'{winner} wins')

def main():
    ask_game = choose_game()

    if ask_game == 'NIM':
        print('Rules:')
        print('1. take as many counters as you want from 1 pile per turn')
        print('2. last person to take a counter loses')
        print('\n')
        cont = input('Press Enter to continue:')
        os.system('cls')
        print('** You are playing against a CPU')
        names = ['','']
        names[0] = input('What is your name? ')
        names[1] = 'CPU'
        game_rendering (names)
        piles = pile_random_gen()
        loser, winner, piles = playing(piles, names)
        winningANDlosing(loser, winner, names, piles)
    elif ask_game == 'roulette':
        print('breh')

main()