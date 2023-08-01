
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


def is_letter(letter):
    """
    Function to validate input is a letter
    """
    if len(letter) > 1:
        return False
    try:
       int(letter)
       return False
    except:
        return True



while True:
    victory = win_condition()
    if victory:
        print('You won!')
        break
    
    letter = input('Type a letter / Word: ')


    check_letter = is_letter(letter)
    if not check_letter and len(letter) == 1:
        print('This is not a letter! Please type again')
        continue

        
    if ATTEMPTS == len(wrong):
        print('You lose!')
        break


    if letter in word:
        right.append(letter)
    else:
        wrong.append(letter)
    

    print('right: ', right)
    print('wrong: ', wrong)
