import random
from time import sleep


def guess_game():


    def guess(x):

        random_number = random.randint(1, x)
        guess = 0

        while guess != random_number:
            guess = int(input(f'Guess a number between 1 and {x}: '))
            if guess == random_number:
                print(f'You won the number is {random_number}!')
            elif guess > x:
                print(f'Your number was higher than the maximum of {x}')
            elif guess < random_number:
                print(f'Your guess ({guess}) was to low!')
            elif guess > random_number:
                print(f'Your guess ({guess} was to high)')
            else:
                print(f'Only thype numbers between 1 and {x} ')

    def computer_guess(x):
        low = 1
        high = x
        feedback = ''
        while feedback != 'c':
            guess = random.randint(low, high)
            feedback = input(f'Is {guess} to high (H), to low (L) or correct(C)? \nAnswer:').lower()
            if feedback == 'h':
                guess - 1
            elif feedback == 'l':
                guess + 1

    try:
        x = int(input('Type the maximum: '))
        guess(x)
        sleep(5)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print('Now it´s the bots turn!')
        computer_guess(x)
    except:
        print(f'There was an error in main.py')

