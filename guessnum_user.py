# Guess the Number (User picks a number, computer guesses)
import random
def comp_guess(x):
    low = 1
    high = x
    feedback = ''
    
    # Computer continues guessing until it gets the correct answer
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # If only one number is left, that's the answer
        
        # Asking user for feedback on the computer's guess
        feedback = input(f"Is {guess} too high (h), too low (l), or correct (c)? ")
        
        if feedback == 'h':
            high = guess - 1  # Adjust range if guess is too high
        elif feedback == 'l':
            low = guess + 1   # Adjust range if guess is too low

    print(f"Yay! The computer guessed your number {guess} correctly!")

# Starting the guessing game with a max range of 200
comp_guess(200)