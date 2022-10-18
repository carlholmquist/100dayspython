from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()
order_name = input(f"What would you like to drink?{menu.get_items()}")
if menu.find_drink(order_name) == None:
    if order_name == "report":
        money.report()
        coffee_maker.report()
    pass
else:
    drink = menu.find_drink(order_name)
    if coffee_maker.is_resource_sufficient(drink):
        money.make_payment(drink.cost)
        print(drink)
        coffee_maker.make_coffee(drink)
