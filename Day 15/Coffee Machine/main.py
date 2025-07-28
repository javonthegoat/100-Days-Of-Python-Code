from tkinter import Menu

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
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def check_resources(coffee):
    enough_resources = True
    if coffee != "espresso":
        if MENU[coffee]["ingredients"]["water"] > resources["water"] and MENU[coffee]["ingredients"]["coffee"] > resources["coffee"] and MENU[coffee]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough water.\nSorry there is not enough coffee.\nSorry there is not enough milk.")
            enough_resources = False
        elif MENU[coffee]["ingredients"]["water"] > resources["water"] and MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough water.\nSorry there is not enough coffee.")
        elif MENU[coffee]["ingredients"]["water"] > resources["water"] and MENU[coffee]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough water.\nSorry there is not enough milk.")
            enough_resources = False
        elif MENU[coffee]["ingredients"]["coffee"] > resources["coffee"] and MENU[coffee]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough coffee.\nSorry there is not enough milk.")
        elif MENU[coffee]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water.")
        elif MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            enough_resources = False
        elif MENU[coffee]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk.")
            enough_resources = False
    else:
        if MENU[coffee]["ingredients"]["water"] > resources["water"] and MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough water.\nSorry there is not enough coffee.")
            enough_resources = False
        elif MENU[coffee]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water.")
            enough_resources = False
        elif MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            enough_resources = False
    return enough_resources

def insert_coins():
    quarters = float(input("Insert quarters: ")) * 25
    dimes = float(input("Insert dimes: ")) * 10
    nickels = float(input("Insert nickels: ")) * 5
    pennies = float(input("Insert pennies: "))
    try:
        total = (quarters + dimes + nickels + pennies) / 100
    except ZeroDivisionError:
        return 0
    return total

def process_transaction(money):
    change = 0
    if money == MENU[coffee_choice]["cost"]:
        resources["money"] += MENU[coffee_choice]["cost"]
    elif money > MENU[coffee_choice]["cost"]:
        change = round(money - MENU[coffee_choice]["cost"], 2)
        resources["money"] += MENU[coffee_choice]["cost"]
    return change

machine_on = True
while machine_on: # keep the machine running
    coffee_choice = input("What would you like? (espresso, latte, cappuccino) ").lower() # Ask the user for their coffee of choice.
    if coffee_choice == "off": # Operator typed 'off'
        print("Powering off...") # Let the operator know the machine is turning off
        machine_on = False # Turn the machine off
    elif coffee_choice == "report": # Operator typed 'report'
        for resource, amount in resources.items(): # loop through the keys and values in the resources dictionary
            if resource == "coffee":
                print(f"{resource.title()}: {amount}g") # print the resource in title case along with its value
            elif resource == "money":
                print(f"{resource.title()}: ${amount}")
            else:
                print(f"{resource.title()}: {amount}ml")
    else:
        resources_available = check_resources(coffee_choice)
        if resources_available:
            money_inserted = insert_coins()
            if money_inserted < MENU[coffee_choice]["cost"]:
                print(f"Sorry ${money_inserted} is not enough. Money refunded.")
            else:
                processed_money = process_transaction(money_inserted)
                if processed_money > 0:
                    print(f"Here is ${processed_money} in change.")
                # make coffee
                for resource, amount in MENU[coffee_choice]["ingredients"].items():
                    resources[resource] -= amount
                print(f"Here is your {coffee_choice} Enjoy!")