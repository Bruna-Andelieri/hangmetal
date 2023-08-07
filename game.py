import random
from hangman import display_hangman
import utils
from data import metal_bands
from colorama import Fore, Style


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
    except ValueError:
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
    # Return True if any of the special characters in
    # special_characters are present in the letter.
    if any(char in special_characters for char in letter):
        return True
    else:
        return False


def build_word(letter, word, build):
    """
    Takes a letter and a word and replaces letters in
    the build that match the letter
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
        message(f"{Fore.LIGHTRED_EX}Spaces are not alowed! Please type again{Style.RESET_ALL}")
        check = False

    check_double_letter = is_duplicated(letter, right, wrong)
    # check if the letter is alredy used
    if check_double_letter:
        message(f"{Fore.LIGHTRED_EX}This letter was alredy used! Please type again{Style.RESET_ALL}")
        check = False

    check_special_character = is_special_character(letter)
    # check if special character is a special character
    if check_special_character:
        message(f"{Fore.LIGHTRED_EX}This is a special character! Please type again{Style.RESET_ALL}")
        check = False

    # check if the letter is a number
    if str(letter).isnumeric():
        message(f"{Fore.LIGHTRED_EX}This is a number, type a letter! Please type again{Style.RESET_ALL}")
        check = False

    check_letter = is_letter(letter)
    # check if the letter is a letter and size equal to 1
    if not check_letter and len(letter) == 1:

        message(f"{Fore.LIGHTRED_EX}This is not a letter! Please type again{Style.RESET_ALL}")
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
    word = get_random_value(metal_bands)
    word_built = "_" * len(word)

    # This function is used to build the band.
    while True:
        victory = win_condition(word, letter, word_built)
        # If victory is true print the build word.
        if victory:
            word_built = word
            win = True
            print(f"{Fore.GREEN}You won!{Style.RESET_ALL} Do you like {Fore.CYAN}{word}{Style.RESET_ALL}?")
            break

        # If attempts_left 0 print the band is the word.
        if attempts_left == 0:
            win = False
            print(f"{Fore.RED}You lose!{Style.RESET_ALL} The band is {Fore.CYAN}{word}{Style.RESET_ALL}?")
            break

        print()
        print(display_hangman(attempts_left))
        print(Fore.LIGHTMAGENTA_EX + word_built + Style.RESET_ALL)
        print()
        print(Fore.LIGHTYELLOW_EX + "Incorrectly guessed letters: ", ", ".join(wrong) + Style.RESET_ALL)
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
