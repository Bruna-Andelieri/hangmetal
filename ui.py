import os

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        

def start_game():
    answer = ""
    while True:
        answer = input('Would you like to start the game? Y/N: ')
        if answer in 'yYnN':
            break

        clear_terminal()
    return answer
       

def win_game():
    print('You Won!')
    anwser = input('Would you like to eplay againa? Y/N: ')
    if anwser in 'yY':
        ...
        

def lose_game():
    print('You Lose!')
    anwser = input('Would you like to eplay againa? Y/N: ')
    if anwser in 'yY':
        clear_terminal() 


def play_game():
    answer = ""
    while True:
        anwser = input('Did you Won or Lose? W/L:')
        if anwser in 'WwlL':
            break
    
    return answer


def main():
    answer = start_game()
    clear_terminal()

    if answer in 'yY':
        play_game()
    elif answer in 'nN':
        start_game()
    


main()
