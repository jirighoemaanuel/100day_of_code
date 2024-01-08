import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# # LIST OF STATES IN NIGERIA
# nigeria_states = [
#     'Abia', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno',
#     'Cross River', 'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'Gombe', 'Imo', 'Jigawa',
#     'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger',
#     'Ogun', 'Ondo', 'Osun', 'Oyo', 'Plateau', 'Rivers', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara'
# ]

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
moves = [rock, paper, scissors]
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_play = int(input())
ai_play = random.randint(0, 2)

print(moves[user_play])
print("Computer Chose:")
print(moves[ai_play])

if user_play == 0 and ai_play == 1:
 print("You Lose")
elif user_play == 1 and ai_play == 0:
 print("You Won")
elif user_play == 1 and ai_play == 2:
 print("You Lose")
elif user_play == 2 and ai_play == 1:
 print("You Won")
else:
 print("It's a Draw")
