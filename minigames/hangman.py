import random
import string
from words import words


def hangman_game():
    def get_valid_word(words):
        word = random.choice(words)
        while '-' in word or ' ' in word:
            word = random.choice(words)
        return word

    def hangman():
        word = get_valid_word(words)
        word_letters = set(word)
        alphabet = set(string.ascii_uppercase)
        used_letters = set()

        user_letter = input('Guess a letter:').upper()

    user_input = input('Type sth:')
    print(user_input)

