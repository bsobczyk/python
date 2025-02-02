from coffee_maker import CoffeeMaker
from menu import Menu,MenuItem
from money_machine import MoneyMachine

is_on = True

machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()
# machine.report()
# coffe_maker.report()


while is_on:
	options = menu.get_items()
	choice = (input(f"What would you like? {options} :").lower()).replace(' ', '')
	if choice == "off":
		is_on=False
		break
	elif choice == "report":
		coffe_maker.report()
		machine.report()
	else:
		drink = menu.find_drink(choice)
		if coffe_maker.is_resource_sufficient(drink) and machine.make_payment(drink.cost):
				coffe_maker.make_coffee(drink)


