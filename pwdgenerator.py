import random

print("---Welcome to your password generator---")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+|}{][|\:;'/?><.,=-~`]}"

number = int(input("Enter the number of passwords you want: "))

length = int(input("Enter the length for password: "))

print("Here are your passwords: ")
for password in range(number):
  password = ""
  for c in range(length):
    password += random.choice(chars)

  print(password)
