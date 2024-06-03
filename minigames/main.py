from guess import guess_game
from hangman import hangman_game
from time import sleep


try:
    while True:
        choose_game = input(int('Which game do you wanna play?\n[1] Guess the number \n[2] Hangman'))
        if choose_game == 1:
            guess_game()
        elif choose_game == 2:
            hangman()
        else:
            print('Bitte gebe eine Gültige nummer ein!')

except:
    print('ERROR in main.py')
