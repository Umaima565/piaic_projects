from words import words 
from live_visuals_dict import hangman_art
import random
import string

def get_valid_word(words):
    word = random.choice(words)
    while " " in word or "-" in word:
      word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
      print("You have used thes letters : ", " ".join(used_letters))


      word_list = [letter if letter in used_letters else "-" for letter in word]
      print(f"You have {lives} lives left ", hangman_art[lives])
      print("Current word: "," ".join(word_list))

      user_letter =input("Guess a letter: ").upper()
      if user_letter in alphabets - used_letters:
          used_letters.add(user_letter)
          if user_letter in word_letters:
            word_letters.remove(user_letter)
            print(" ")

          else:
            lives = lives - 1
            print(f"Your letter {user_letter} is not in the word")

      elif user_letter in used_letters:
        print("You have already used that letter. Try again")

      else:
        print("Invalid character. Try again")

    if lives == 0:
      print(hangman_art[lives])
      print(f"You lost/die. SORRY The word was: {word}")

    else:
      print(f"Hurray!! You won you guessed the word: {word}")

hangman()