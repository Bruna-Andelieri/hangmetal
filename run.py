import os

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def question(message, criteria):
    msg = ""
    while True:
        msg = input(message)
        if msg in criteria:
            break

        clear_terminal()
    return msg


def start_game():
    return question('Would you like to start the game? Y/N: ', 'yYnN')
  

def win_game():
    print('You Won!')
    return question('Would you like to play againa? Y/N: ', 'yYnN')

def lose_game():
    print('You Lose!')
    return question('Would you like to play againa? Y/N: ', 'yYnN')


def play_game():
    msg = ""
    while True:
        msg = input('Did you Won or Lose? W/L:')
        if msg in 'WwlL':
            break
    
    return msg


initial = True
msg = ""

while True:
    clear_terminal()
    
    if initial:
        msg = start_game()

    if msg in 'nN':
        break
    
    msg = play_game()
    if msg in 'Ww':
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
            
