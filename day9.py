import os

# You can call clear() to clear the output in the console.
def clear():
 os.system('cls')


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bidder_list = []

def add_bidder():
    name = input("What is your name?: ")
    bid = int(input(f"What is {name}'s bid?: $"))
    bidder_list.append({"name": name, "bid": bid})

while True:
    add_bidder()
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if other_bidder == 'no':
        break
    clear()

highest_bidder = max(bidder_list, key=lambda x: x["bid"])
print(f"The winner is {highest_bidder['name']} with a bid of ${highest_bidder['bid']}")
