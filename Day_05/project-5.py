# Project - 5, 
# Password generator using letters and numbers
# Provide the length of the password
# How many letters, numbers and symbol you want in your password
# using the random.suffle to reorder the list,

import random

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the pyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy level
# password =""
# # nr_letters =4
# for char in range(1, nr_letters+1):

#     password  += random.choice(letters)

# for char in range(1, nr_symbols+1):
#     password += random.choice(symbols)

# for char in range(1, nr_numbers+1):
#     password += random.choice(numbers)

# print(password)
  

# Hard level

password_list =[]
# nr_letters =4
for char in range(1, nr_letters+1):

    password_list.append(random.choice(letters))

for char in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))

for char in range(1, nr_numbers+1):
    password_list.append(random.choice(numbers))

# print(password_list)
random.shuffle(password_list)
# print(password_list)

passwd =""
for char in password_list:
    passwd += char

print(f"Your new generated password is: {passwd}")


   
    