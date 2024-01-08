#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = []

# Generate and append letters to password
for i in range(nr_letters):
 password.append(letters[random.randint(1, len(letters)-1)])
 # Generate and append symbols to password
for i in range(nr_symbols):
 password.append(symbols[random.randint(1, len(symbols)-1)])
 # Generate and append numbers to password
for i in range(nr_numbers):
 password.append(numbers[random.randint(1, len(numbers)-1)])

# Shuffle password list
random.shuffle(password)
# Convert password list to string
password = ''.join(password)
print(password)
