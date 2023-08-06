import game
import utils
import animations


def question(message):
    msg = ""
    while True:
        msg = input(message)
        if msg in 'yYnN':
            break

        utils.clear_terminal()
        print("-> incorrect entry, try again")
    return msg


def screen_start_game():
    utils.clear_terminal()
    animations.hangmetal_ascii_art()
    utils.rules_hangmetal()
    return question(message='Would you like to start the game? Y/N: ')
  

def screen_win_game():
    utils.clear_terminal()
    animations.win_game_ascii_art()
    return question(message='Would you like to play again? Y/N: ')

def screen_lose_game():
    utils.clear_terminal()
    animations.lose_game_ascii_art()
    return question(message='Would you like to play again? Y/N: ')


def screen_play_game():
    utils.clear_terminal()
    return game.run()


def main():
    initial = True
    msg = ""

    while True:
        if initial:
            msg = screen_start_game()

        if msg in 'nN':
            break
        
        result = screen_play_game()
        if result:
            msg = screen_win_game()
            if msg in 'yY':
                initial = False
                continue
            else:
                initial = True

        else:
            msg = screen_lose_game()
            if msg in 'yY':
                initial = False
                continue
            else:
                initial = True
                

main()