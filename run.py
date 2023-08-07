import game
import utils
import animations


def rules_hangmetal():
    print()
    print("                     Guess the hidden Metal band!")
    print("              The aim of the game is to guess the word")
    print("                    Please guess a letter or a word")
    print("            by typing it on the keyboard and pressing enter")
    print("              You have 5 attempts before the man is hang !")
    print()
    print()


def question(message):
    """
    Ask the user for a question. It will return the user's input if it is yYnN or yYnN
    """
    msg = ""
    # input message and try again
    while True:
        msg = input(f" -> {message}")
        if msg in "yYnN":
            break

        utils.clear_terminal()
        print("-> incorrect entry, try again")
    return msg


def screen_start_game():
    """
    Starts the game and asks the user if he wants to start.
    """
    utils.clear_terminal()
    animations.hangmetal_ascii_art()
    rules_hangmetal()
    return question(message="Would you like to start the game? Y/N: ")


def screen_win_game():
    """
    Show screen when user Win the game
    """
    animations.win_game_ascii_art()
    response = question(message="Would you like to play again? Y/N: ")
    utils.clear_terminal()
    return response


def screen_lose_game():
    """
    Show screen when user lose the game
    """

    animations.lose_game_ascii_art()
    response = question(message="Would you like to play again? Y/N: ")
    utils.clear_terminal()
    return response


def screen_play_game():
    """
    Show game screen
    """
    utils.clear_terminal()
    return game.run()


def show_game_result(win):
    """
    SHow wil or loose screen depending the of the game result
    """
    if win:
        msg = screen_win_game()
    else:
        msg = screen_lose_game()

    if msg in "yY":
        initial = False
    else:
        initial = True

    return initial


def main():
    """
    Function to starts the game
    """

    initial = True
    msg = ""

    while True:
        # check if its inital loop. If its true, show the start game screen
        if initial:
            msg = screen_start_game()

        if msg in "nN":
            break

        # run game. Returns True if win or False if lose
        result = screen_play_game()

        # show game result
        initial = show_game_result(result)


    utils.clear_terminal()
    print("Feel free to return whenever you feel prepared!")
main()
