from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

choice = ''

while choice !="off":
    choice = input(f"What do you want? {menu.get_items()} ")
    if choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    if choice in menu.get_items():
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink):
            if moneyMachine.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)