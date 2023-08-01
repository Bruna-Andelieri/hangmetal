
right = []
wrong = []
letter = ''
word = 'azul'
ATTEMPTS = 5

def win_condition():
    """
    Function to check the win condition
    """
    if letter == word:
        return True

    if len(right) == len(word):
        return True



while True:
    letter = str(input('Type a letter: '))

    victory = win_condition()
    if victory:
        print('You won!')
        break

        
    if ATTEMPTS == len(wrong):
        print('You lose!')
        break


    if letter in word:
        right.append(letter)
    else:
        wrong.append(letter)
    

    print('right: ', right)
    print('wrong: ', wrong)
