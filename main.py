"""
LEVEL : B E G I N N E R.
-----------------------------------------------------------
Project - Pass-Word Generator.🔐
-----------------------------------------------------------
Module:
* random - random is a built-in module of the Python programming language.

Functions Used:
* Print - Prints a string into the console. || ex: print("Hello World").
* Input - Prints a string into the console, and asks the user for a string input. || ex: name = input("What's your name").

Loops:
* For loop
--------------------------------------------------------------------------------------------------------------------------
IMP Note : There are two level both will generate password but in eazy the password created in list will not get shuffel
           so hard level is also there to just know how to use random.shuffel to shuffel the list go and check it out.
           !! KEEP STARVING FOR WHAT YOU WANT TO ACCHIEVE !!
"""

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)


#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")