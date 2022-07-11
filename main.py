from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
moneymachine = MoneyMachine()
coffeemaker  = CoffeeMaker()
serving = True
while serving:
    prompt = input(f"What would you like? {menu.get_items()}:")
    if prompt == "off":
        serving = False
    elif prompt == "report":
        coffeemaker.report()
        moneymachine.report()
        pass
    else:
        drink = menu.find_drink(prompt)
        if coffeemaker.is_resource_sufficient(drink)== True and  moneymachine.make_payment(drink.cost) == True:
            coffeemaker.make_coffee(drink)


