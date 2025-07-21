import os
from art import logo

def clear_console():
    if os.name == "nt": # For Windows Operating Systems
        os.system("cls")
    else:
        os.system("clear") # Linux, macOS, and other Unix-like systems

print(logo)
print("Welcome to the silent auction.")

bidders = {}
bidding = True
while bidding:
    bidders_name = input("What is your name? ")
    bid_amount = float(input("What is your bid amount? "))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    bidders[bidders_name] = bid_amount
    if other_bidders == "yes":
        clear_console()
        print(logo)
    else:
        highest_bid = 0
        highest_bidder = ""
        for bidder in bidders:
            amount = bidders[bidder]
            if amount > highest_bid:
                highest_bid = amount
                highest_bidder = bidder
        clear_console()
        print(logo)
        print(f"{highest_bidder} has won with the highest bid amount of ${highest_bid}")
        bidders = {}