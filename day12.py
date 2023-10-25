import random
import os


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


if level == 'easy':
 lives = 10
else:
 lives = 5
print(f"You have {lives} attemots remaining to guess the number.")
number = random.randint(1, 100)
guess = int(input("Make a guess: "))

while True:
 if guess > number:
  print("Too high.\n")
 elif guess < number:
  print("Too low")
 else:
  print("You win!")
 lives -= 1
 if lives == 0:
  print("You've run out of guesses, you lose")
  break
 print("Guess again.")
 print(f"You have {lives} attemots remaining to guess the number.")
 guess = int(input("Make a guess: "))