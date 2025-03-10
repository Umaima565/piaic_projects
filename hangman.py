# Hangman Game
import random
from words import words  # Importing words list
from live_visuals_dict import hangman_art  # Importing hangman visuals
import string

def get_valid_word(words):
    word = random.choice(words)
    while " " in word or "-" in word:  # Ensuring we get a single valid word
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Letters in the chosen word
    alphabets = set(string.ascii_uppercase)
    used_letters = set()  # Letters guessed so far
    lives = 7  # Player starts with 7 lives
    
    while len(word_letters) > 0 and lives > 0:
        print("You have used these letters: ", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(f"You have {lives} lives left", hangman_art[lives])
        print("Current word: ", " ".join(word_list))
        
        # User inputs a guess
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1  # Incorrect guess reduces a life
                print(f"Your letter {user_letter} is not in the word")
        elif user_letter in used_letters:
            print("You have already used that letter. Try again.")
        else:
            print("Invalid character. Try again.")
    
    # Game over messages
    if lives == 0:
        print(hangman_art[lives])
        print(f"You lost. The word was: {word}")
    else:
        print(f"Hurray!! You won! The word was: {word}")

hangman()
