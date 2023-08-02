import os
import game

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def question(message):
    msg = ""
    while True:
        msg = input(message)
        if msg in 'yYnN':
            break

        clear_terminal()
    return msg


def start_game():
    return question(message='Would you like to start the game? Y/N: ')
  

def win_game():
    print('You Won!')
    return question(message='Would you like to play againa? Y/N: ')

def lose_game():
    print('You Lose!')
    return question(message='Would you like to play againa? Y/N: ')


initial = True
msg = ""

while True:
    clear_terminal()
    
    if initial:
        msg = start_game()

    if msg in 'nN':
        break
    
    result = game.run()
    if result:
        msg = win_game()
        if msg in 'yY':
            initial = False
            continue
        else:
            initial = True

    else:
        msg = lose_game()
        if msg in 'yY':
            initial = False
            continue
        else:
            initial = True
            
