from data import metal_bands
import random



ATTEMPTS = 5

def get_random_value(list_values):
    return random.choice(list_values)

def win_condition(word, letter, right):
    """
    Function to check the win condition
    """
    if letter.lower() == word.lower():
        return True

    if len(right) == len(word):
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


def run():
    right = []
    wrong = []
    letter = ''
    win = False

    word = "Sepultura"  #  get_random_value(metal_bands)

    while True:
        victory = win_condition(word, letter, right)
        if victory:
            win = True
            print('You won!', f"Do you like {word}?")
            break
            
        if ATTEMPTS == len(wrong):
            win = False
            print('You lose!', f"The band is {word}")
            break

        letter = input('Type a letter / Word: ').strip()

        if not letter:
            print('Spaces are not alowed! Please type again')
            continue

        check_double_letter = is_duplicated(letter, right, wrong)
        if check_double_letter:
            print('This letter was alredy used! Please type again')
            continue

        check_special_character = is_special_character(letter)
        if check_special_character:
            print('This is a special character! Please type again')
            continue

        if str(letter).isnumeric():
            print('This is a number, type a letter! Please type again')
            continue

        check_letter = is_letter(letter)
        if not check_letter and len(letter) == 1:
            print('This is not a letter! Please type again')
            continue



        if letter.lower() in word.lower():
            right.append(letter.lower())
        else:
            wrong.append(letter.lower())
        

        print('right: ', ", ".join(right))
        print('wrong: ', ", ".join(wrong))


    return win

