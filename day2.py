# # 1st input: enter height in meters e.g: 1.65
# height = float(input())
# # 2nd input: enter weight in kilograms e.g: 72
# weight = float(input())

# bmi = weight / (height**2)
# print(int(bmi))

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage of tip would you give? 10, 12, or 15? "))
numPeople = int(input("How many people to split the bill? "))

percentBill = bill * tip/100
TotalBill = bill + percentBill
amountPerPerson = TotalBill/numPeople

print(f"Each person should pay {round(amountPerPerson, 2)}")