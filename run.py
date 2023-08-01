
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
    try:
       int(letter)
       return False
    except:
        if len(letter) > 1:
            return False
        else:
            return True
    


def is_duplicated(letter):
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



while True:
    victory = win_condition()
    if victory:
        print('You won!')
        break
        
    if ATTEMPTS == len(wrong):
        print('You lose!')
        break

    letter = input('Type a letter / Word: ').strip()

    if not letter:
        print('Spaces are not alowed! Please type again')
        continue

    check_double_letter = is_duplicated(letter)
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

    if letter in word:
        right.append(letter)
    else:
        wrong.append(letter)
    

    print('right: ', right)
    print('wrong: ', wrong)
