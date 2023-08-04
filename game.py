import random
from hangman import display_hangman
import utils
from data import metal_bands


attempts = 6

def get_random_value(list_values):
    return random.choice(list_values)

def win_condition(word, letter, build):
    """
    Function to check the win condition
    """
    if letter.lower() == word.lower():
        return True

    if "".join(build).lower() == word.lower():
        return True


def is_letter(letter):
    """
    Function to validate input is a letter
    """
    try:
       int(letter)
       return False
    except:
        if len(letter) > 1:
            return False
        else:
            return True
    

def is_duplicated(letter, right, wrong):
    if letter in wrong:
        return True
    
    if letter in right:
        return True
    return False


def is_special_character(letter):
    special_characters = "!@#$%^&*()-+?_=,<>/"
    if any(char in special_characters for char in letter):
        return True
    else:
        return False

def build_world(letter, word, build):
    word_as_list = list(build)

    for num, l in enumerate(word):
        if letter.lower() == l.lower():
            word_as_list.pop(num)
            word_as_list.insert(num, letter)

    return word_as_list

def run():
    right = []
    wrong = []
    letter = ''
    win = False
    attempts_left = attempts
    

    word = get_random_value(metal_bands)
    build = "_" * len(word)

    while True:
        victory = win_condition(word, letter, build)
        if victory:
            build = word
            win = True
            print('You won!', f"Do you like {word}?")
            break
            
        if attempts_left == 0:
            win = False
            print('You lose!', f"The band is {word}")
            break


        if not letter:
            print('Spaces are not alowed! Please type again')
            

        check_double_letter = is_duplicated(letter, right, wrong)
        if check_double_letter:
            print('This letter was alredy used! Please type again')
            

        check_special_character = is_special_character(letter)
        if check_special_character:
            print('This is a special character! Please type again')
            

        if str(letter).isnumeric():
            print('This is a number, type a letter! Please type again')
            

        check_letter = is_letter(letter)
        if not check_letter and len(letter) == 1:
            print('This is not a letter! Please type again')
            

        if letter.lower() in word.lower():
            word_as_list = build_world(letter, word, build)
            build = "".join(word_as_list)

            right.append(letter.lower())

        else:
            wrong.append(letter.lower())
            attempts_left -= 1
            
        
        
        print(display_hangman(attempts_left))
        print(build)
        print('right: ', ", ".join(right))
        print('wrong: ', ", ".join(wrong))
        letter = input('Type a letter / Word: ').strip()
        utils.clear_terminal()


    return win

