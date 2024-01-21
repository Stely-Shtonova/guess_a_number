from random import randint
# colors
Red = '\033[31m'
Green = '\033[32m'
Orange = '\033[33m'
Blue = '\033[34m'
Purple = '\033[35m'
Magenta = '\033[35m'

# the computer chooses a random number between 1 and 100
computers_number = randint(1, 100)
while True:
    # getting user's input
    your_guess = input(Green + 'Guess the number chosen by the computer (1 - 100):\n')
    # checking if the user's guess is an integer and if it's within the requirements
    if not your_guess.isdigit():
        print('Invalid input! Please try again...')
        continue
    elif int(your_guess) > 100 or int(your_guess) < 1:
        print('Invalid input! Please try again...')
        continue
    # comparing numbers
    if int(your_guess) == computers_number:
        print(Magenta + 'Congratulations! The computer chose the number ' \
              + Red + str(computers_number) + Magenta + ' and you guessed it!')
        break
    else:
        print(Blue + 'Not quite...')
        # dropping hints
        if int(your_guess) > computers_number:
            print(Purple + 'Try with a smaller number...')
            continue
        elif int(your_guess) < computers_number:
            print(Purple + 'Try with a bigger number...')
            continue
