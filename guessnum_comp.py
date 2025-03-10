import random
secret_num : int = random.randint(1, 100)

print("I am thinking of a number b/w 1 and 100.")

guess_number = int(input("enter your guess: "))


while guess_number  != secret_num:
  if guess_number > secret_num:
    print("your guess is too high! try again.")
  else:
    print("your guess is too low! try again.")

  guess_number = int(input("enter another guess: "))

  

print(f"HURRAH! you found the number. it was {secret_num}")
