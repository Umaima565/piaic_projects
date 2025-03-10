import random 

def play():
    print("Let's play Rock, Paper, Scissors!")  # Game start message
    
    # Taking user input for their choice
    user = input("'r' for Rock, 'p' for Paper, 's' for Scissors: ")  
    computer = random.choice(['r', 'p', 's'])  # Randomly choosing for the computer

    if user == computer:
        return "It's a tie!"  # If both choose the same, it's a tie

    if win(user, computer):  
        return "You won!!"  # If user wins, return winning message

    return "You lost!!"  # Otherwise, the user lost

def win(player, opponent):
    # Checking the winning conditions
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

print(play())  # Running the game
