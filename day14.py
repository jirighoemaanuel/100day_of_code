# from art import logo, vs
# from game_data import data
# from random import choice, randint
# import os


# def clear():
#     os.system("cls")


# print(logo)
# updated_compare = None
# final_score = 0
# compare = choice(data)

# while True:
#     against = choice(data)
#     print(
#         f"Compare A: {compare['name']}, a {compare['description']}, from {compare['country']}.")
#     print(vs)
#     print(
#         f"Against B: {against['name']}, a {against['description']}, from {against['country']}.")
#     user_ans = input("Who has more followers? Type 'A' or 'B': ").lower()
#     if user_ans == 'a' and compare['follower_count'] > against['follower_count']:
#         clear()
#         print(logo)
#         compare = against
#         final_score += 1
#         print(f"You're right! Current score: {final_score}")
#         continue
#     elif user_ans == 'b' and against['follower_count'] > compare['follower_count']:
#         clear()
#         print(logo)
#         compare = against
#         final_score += 1
#         print(f"You're right! Current score: {final_score}")
#         continue
#     else:
#         clear()
#         print(logo)
#         print(f"Sorry, that's wrong. Final score: {final_score}")
#         break

from art import logo, vs
from game_data import data
from random import choice
import os


def clear():
    os.system("cls")


score = 0
game_over = False
compare = choice(data)


def display_person(person):
    return f"{person['name']}, a {person['description']}, from {person['country']}."


while not game_over:
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {display_person(compare)}")
    print(vs)
    against = choice(data)
    print(f"Against B: {display_person(against)}")
    user_ans = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_ans == 'a':
        winner = 'a' if compare['follower_count'] > against['follower_count'] else 'b'
    else:
        winner = 'b' if against['follower_count'] > compare['follower_count'] else 'a'

    if user_ans == winner:
        clear()
        score += 1
        compare = against
    else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
