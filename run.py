import game
import utils
import animations


def question(message):
    """
     Ask the user for a question. It will return the user's input if it is yYnN or yYnN
    """
    msg = ""
    # input message and try again
    while True:
        msg = input(message)
        if msg in 'yYnN':
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
    utils.rules_hangmetal()
    return question(message='Would you like to start the game? Y/N: ')
  

def screen_win_game():
    """
    Show screen when user Win the game
    """
    utils.clear_terminal()
    animations.win_game_ascii_art()
    return question(message='Would you like to play again? Y/N: ')

def screen_lose_game():
    """
    Show screen when user lose the game
    """

    utils.clear_terminal()  
    animations.lose_game_ascii_art() 

    return question(message='Would you like to play again? Y/N: ')


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

    if msg in 'yY':
        play_again = False
    else:
        play_again = True

    return play_again


def main():
    """
    Function to starts the game
    """

    play_again = True
    msg = ""


    while True:
        # check if its inital loop. If its true, show the start game screen
        if play_again:
            msg = screen_start_game()

        if msg in 'nN':
            break
        
        # run game. Returns True if win or False if lose
        result = screen_play_game()

        # show game result
        play_again = show_game_result(result)

main()