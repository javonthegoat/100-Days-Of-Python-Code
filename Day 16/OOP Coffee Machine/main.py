from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine() # Initialize the money machine
coffee_machine = CoffeeMaker() # Initialize the coffee maker
coffee_menu = Menu() # Initialize the coffee menu

# keep the machine running until turned off
machine_on = True
while machine_on:
    coffee_choice = input(f"What would you like? {coffee_menu.get_items()}: ").lower() # typing "off" turns the machine off, typing "report" prints the machines resources
    # turn the machine off
    if coffee_choice == "off":
        machine_on = False
    # print the avilable resources and profit
    elif coffee_choice == "report":
        coffee_machine.report()
        if money.profit > 0:
            money.report()
    else:
        # check if the drink is available
        coffee = coffee_menu.find_drink(coffee_choice)
        # make the coffee if there are enough resources and the payment is successful
        if coffee_machine.is_resource_sufficient(coffee):
            if money.make_payment(coffee.cost):
                coffee_machine.make_coffee(coffee)