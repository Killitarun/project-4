#This program lets you to create your password
#This program also helps you to generate different different passwords at a time

print("-------WELCOME TO PASSWORD GENERATOR PROGRAM-------\n")

import random
import string

#Function to generate a random password
def generate_password(num_letters, num_digits, num_symbols):
    letters = ''.join(random.choices(string.ascii_letters, k=num_letters))
    digits = ''.join(random.choices(string.digits, k=num_digits))
    symbols = ''.join(random.choices(string.punctuation, k=num_symbols))

    password = list(letters + digits + symbols)
    random.shuffle(password)
    main_password = ''.join(password)
    
    return main_password

#Taking input from the user
num_letters = int(input("Enter the number of letters you want in the password: ")) 
num_digits = int(input("Enter the number of digits you want in the password: "))
num_symbols = int(input("Enter the number of symbols you want in the password: "))
num_passwords = int(input("Enter the number of passwords you want to generate: "))

#Generating passwords and printing them
for i in range(num_passwords):
    password = generate_password(num_letters, num_digits, num_symbols)
    print(f"\nyour Password {i+1}: ",password)
