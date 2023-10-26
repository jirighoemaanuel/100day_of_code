from art import logo, vs
from game_data import data
from random import choice, randint
import os


def clear():
    os.system("cls")


print(logo)
updated_compare = None
final_score = 0
compare = choice(data)

while True:
    against = choice(data)
    print(
        f"Compare A: {compare['name']}, a {compare['description']}, from {compare['country']}.")
    print(vs)
    print(
        f"Against B: {against['name']}, a {against['description']}, from {against['country']}.")
    user_ans = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_ans == 'a' and compare['follower_count'] > against['follower_count']:
        compare = compare
        final_score += 1
        print(f"You're right! Current score: {final_score}")
        continue
    elif user_ans == 'b' and against['follower_count'] > compare['follower_count']:

        final_score += 1
        print(f"You're right! Current score: {final_score}")
        continue
    else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {final_score}")
        break
