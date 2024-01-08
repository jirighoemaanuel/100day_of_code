import os

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)
num1 = int(input("What's the first number?: "))
print("+\n-\n*\n/")
operation = input("Pick an operation: ")
num2 = int(input("What's the next number?: "))



def clear():
 os.system("cls")



# cal_value = 0
def calulator(a, b, opera):
 if opera == "+":
  result = a + b
  return result
 elif opera == "-":
  result = a - b
  return result
 elif opera == "*":
  result = a * b
  return result
 elif opera == "/":
  result = a / b
  return result

calc_value = 0 


while True:
 calc_value = calulator(num1, num2, operation)
 print(f"{num1} {operation} {num2} = {calc_value}")
 response = input(f"Type 'y' to continue calculating with {calc_value}, or type 'n' to start a new calculation: ")
 if response == "y":
  cal_value = int(calc_value)
  num1 = cal_value
  operation = input("Pick an operation: ")
  num2 = int(input("What's the next number?: "))
 elif response == 'n':
  calc_value = 0
  clear()
  print(logo)
  num1 = int(input("What's the first number?: "))
  print("+\n-\n*\n/")
  operation = input("Pick an operation: ")
  num2 = int(input("What's the next number?: "))
  continue