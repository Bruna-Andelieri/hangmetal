
right = []
wrong = []
letter = ''
word = 'azul'
ATTEMPTS = 6
while True:
    letter = str(input('Type a letter: '))

    if letter == word:
        print('You won!')
        break

    if letter in word:
        right.append(letter)
    else:
        wrong.append(letter)
    
    if ATTEMPTS == len(wrong):
        print('You lose!')
        break

    if len(right) == len(word):
        print('You won!')
        break

    print('right: ', right)
    print('wrong: ', wrong)

    