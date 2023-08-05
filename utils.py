import os

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def rules_hangmetal():
    print("The computer chooses a random Band! Your goal is to guess which band it is. This game is perfect for testing your knowledge in Metal! Please guess a letter or a word (if you already have an idea what it could be) by typing it on the keyboard and pressing enter. You have 5 attempts to guess the band correctly. If you don't succeed, you can try again.")