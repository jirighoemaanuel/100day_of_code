# # Rollercoaster ticket logic
# print("Welcome to the rollercoster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#  print("You can ride the rollercoaster")
#  age = int(input("What is your age?"))
#  if age <= 12:
#   bill = 5
#   print("Child tickets are $5.")
#  elif age <= 18:
#   bill = 7
#   print("Youth tickets are $7.")
#  elif age >= 45 and age <= 55:
#   print("You get a free ride on us")
#  else:
#   bill = 12
#   print("Adult tickets are $12.")
#  wants_photo = input("Do you want a photo taken? Y or N. ").lower()
#  if wants_photo == "y":
#   bill += 3

#  print(f"Your final bill is {bill}")
# else:
#  print("You height is not enough to take this ride")


# ODD or EVEN NUMBER
# Which number do you want to check?
# number = int(input("Which number do you want to check?"))
# if (number % 2) == 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


print('You\'re at a cross road. Where do you want to go? Type "left" or "right"')
direction = input()
if direction == "left":
 print('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for boat. Type "swim" to swim across.')
 decision = input()
 if decision == "wait":
  print("You arrive at the island unharmed.There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
  door_chosen = input()
  if door_chosen == "yellow":
   print("CONGRATULATIONS. YOU WON!!!")
  elif door_chosen == "red":
   print("You are Burned by fire. GAME OVER.")
  elif door_chosen == "Blue":
   print("You are Eaten by Beasts. GAME OVER.")
  else:
   print("GAME OVER.")
 else:
  print("You are attacked by trout. GAME OVER.")
else:
 print('You fall into a hole. GAME OVER.')