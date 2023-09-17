from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
cm = CoffeeMaker()
mm=MoneyMachine()

is_on = True
while is_on:
    choice = input(f"What would you like? {menu.get_items()}??: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        cm.report()
    else:
        drink = menu.find_drink(choice)
        print(drink)
        if cm.is_resource_sufficient(drink):
            # payment = process_coins()
            if mm.make_payment(drink.cost):
                cm.make_coffee(drink)

