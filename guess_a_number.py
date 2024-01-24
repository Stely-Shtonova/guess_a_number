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
attempts_count = 0
have_guessed = False
while True:
    # getting user's input
    your_guess = input(Green + 'Guess the number chosen by the computer (1 - 100):\n')
    # checking if the user's guess is an integer and if it's within the requirements
    if not your_guess.isdigit():
        print(Red + 'Invalid input! Please try again...')
        continue
    elif int(your_guess) > 100 or int(your_guess) < 1:
        print(Red + 'Invalid input! Please try again...')
        continue
    else:
        attempts_count += 1
    # comparing numbers
    if int(your_guess) == computers_number:
        print(Magenta + 'Congratulations! The computer chose the number ' + \
            Red + str(computers_number) + Magenta + f' and you guessed it on the ' + \
            Red + str(attempts_count) + Magenta + ' try!')
        have_guessed = True
    else:
        print(Blue + 'Not quite...')
        # dropping hints
        if int(your_guess) > computers_number:
            print(Purple + 'Try with a smaller number...')
        elif int(your_guess) < computers_number:
            print(Purple + 'Try with a bigger number...')
    while have_guessed:
        # prompting the user to play again
        print(Blue + 'Would you like to play again?')
        answer = input(Blue + 'Answer with [yes] or [no]: ')
        if answer.lower() == 'yes':
            attempts_count = 0
            computers_number = randint(1, 100)
            have_guessed = False
            break
        elif answer.lower() == 'no':
            print(Blue + 'Thanks for playing...')
            raise SystemExit
        else:
            print(Red + 'Invalid input!')
            continue
    # checking if the attempts are over the limit
    while attempts_count == 3:
        # prompting the user to play again
        print(Purple + f'You lost- you have no more tries left. The number was {computers_number}. Would you like to play again?')
        answer = input(Orange + 'Answer with [yes] or [no]: ')
        if answer.lower() == 'yes':
            attempts_count = 0
            computers_number = randint(1, 100)
            break
        elif answer.lower() == 'no':
            print(Blue + 'Thanks for playing...')
            raise SystemExit
        else:
            print(Red + 'Invalid input!')
            continue
