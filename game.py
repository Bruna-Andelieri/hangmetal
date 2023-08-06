import random
from hangman import display_hangman
import utils
from data import metal_bands


def get_random_value(list_values):
    """
    Get a random value from a list
    """
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
    """
    Checks if letter is duplicated in right and wrong arrays
    """

    if letter in wrong:
        return True

    if letter in right:
        return True
    return False


def is_special_character(letter):
    """
    Checks if a letter is a special character
    """
    special_characters = "!@#$%^&*()-+?_=,<>/"
    # Return True if any of the special characters in special_characters are present in the letter.
    if any(char in special_characters for char in letter):
        return True
    else:
        return False


def build_word(letter, word, build):
    """
    Takes a letter and a word and replaces letters in the build that match the letter
    """
    word_as_list = list(build)

    # Add a letter to word_as_list.
    for num, l in enumerate(word):
        # Add letter to word_as_list.
        if letter.lower() == l.lower():
            word_as_list.pop(num)
            word_as_list.insert(num, letter)

    return word_as_list


def message(msg):
    """
    Clean terminal and print a message
    """
    utils.clear_terminal()
    print(msg)


def validation(letter, right, wrong):
    """
    Checks to make sure the letter is valid
    """
    check = True
    # check if spaces are not alowed
    if not letter:
        message("Spaces are not alowed! Please type again")
        check = False

    check_double_letter = is_duplicated(letter, right, wrong)
    # check if the letter is alredy used
    if check_double_letter:
        message("This letter was alredy used! Please type again")
        check = False

    check_special_character = is_special_character(letter)
    # check if special character is a special character
    if check_special_character:
        message("This is a special character! Please type again")
        check = False

    # check if the letter is a number
    if str(letter).isnumeric():
        message("This is a number, type a letter! Please type again")
        check = False

    check_letter = is_letter(letter)
    # check if the letter is a letter and size equal to 1
    if not check_letter and len(letter) == 1:
        message("This is not a letter! Please type again")
        check = False

    return check


def run():
    """
    Run the Hangmetal game.
    """
    right = []
    wrong = []
    letter = ""
    win = False
    attempts_left = 6
    word = "angra"  # get_random_value(metal_bands)
    word_built = "_" * len(word)

    # This function is used to build the band.
    while True:
        victory = win_condition(word, letter, word_built)
        # If victory is true print the build word.
        if victory:
            word_built = word
            win = True
            print("You won!", f"Do you like {word}?")
            break

        # If attempts_left 0 print the band is the word.
        if attempts_left == 0:
            win = False
            print("You lose!", f"The band is {word}")
            break

        print()
        print(display_hangman(attempts_left))
        print(word_built)
        print()
        print("Incorrectly guessed letters: ", ", ".join(wrong))
        print()
        print()
        letter = input("-> Type a letter / Word: ").strip()
        utils.clear_terminal()

        check = validation(letter, right, wrong)

        # Check if letter is valid
        if not check:
            continue

        # if letter is valid, build the word
        if letter:
            if letter.lower() in word.lower():
                word_as_list = build_word(letter, word, word_built)
                word_built = "".join(word_as_list)
                right.append(letter.lower())

            else:
                wrong.append(letter.lower())
                attempts_left -= 1

    return win
