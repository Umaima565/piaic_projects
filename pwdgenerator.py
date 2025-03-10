import random 

# Welcoming the user to the password generator
print("--- Welcome to your Password Generator ---")

# Defining characters to use in the password
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+|}{][|\\:;'/?><.,=-~`]}"  

# Asking the user how many passwords they want
number = int(input("Enter the number of passwords you want: "))

# Asking for the length of each password
length = int(input("Enter the length for password: "))

# Generating and displaying passwords
print("Here are your passwords:")
for password in range(number):  
    # Creating a random password of the specified length
    password = "".join(random.choice(chars) for _ in range(length))  
    print(password)  # Printing each generated password
