import random

def play():
    print("Lets play rock, paper and scissor")
    user = input("'r' for rock, 'p' for paper and 's' for scissor: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
      return 'Its a tie!'


    if win(user, computer):
        return 'You won!!'

    else:
        return 'You lost!!'

def win(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
      or (player == 'p' and opponent == 'r'):
      return True

print(play())