import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
}


def clear():
    os.system('cls')


drink_list = [i for i in MENU.keys()]


def prompt():
    coffee_type = input("What would you like? (espresso/latte/cappuccono): ")
    if coffee_type in drink_list:
        return coffee_type
    return "We don't have that coffee drink"


def calculate_coin(prompt_res):
    quarters = int(input("How many quarters?: "))
    dime = int(input("How many dime?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_amount = (0.25*quarters) + (0.1*dime) + \
        (0.05*nickles) + (0.01*pennies)
    bal = round((total_amount - MENU[prompt_res]['cost']), 2)
    return bal


def make_coffee(resources, ingre):
    exhau_resourc = None
    for resource in resources.keys():
        if resource == "milk" and user_respnse == "espresso":
            continue
        if resources[resource] < ingre[user_respnse]['ingredients'][resource]:
            exhau_resourc = resource
    if exhau_resourc:
        print(f"Sorry, we're out of {exhau_resourc}.")
    else:
        for resource in resources.keys():
            if resource == "milk" and user_respnse == "espresso":
                continue
            resources[resource] -= ingre[user_respnse]['ingredients'][resource]
    return exhau_resourc


while True:
    user_respnse = prompt()
    cal_coin = calculate_coin(user_respnse)

    if cal_coin < 0:
        print("Sorry that's not enough money. Money refunded.")
        continue
    elif cal_coin > 0:
        print(f"Here is ${cal_coin} in change.")
        resource = make_coffee(resources, MENU)
        if resource:
            print(f"Sorry there is not enough {resource}")
        else:
            print(f"Here is your {user_respnse}, enjoy!")
    print(resources)
