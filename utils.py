import os

ROWSIZE = 80

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def rules_hangmetal():
    print()
    print('                     Guess the hidden Metal band!')
    print('              The aim of the game is to guess the word')
    print('                    Please guess a letter or a word')
    print('            by typing it on the keyboard and pressing enter')
    print('              You have 5 attempts before the man is hang !')
    print()
    print()