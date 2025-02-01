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
}
profit=0
is_on = True

while is_on:
#TODO: 1. Print request_port
    user_choice = (input("What would you like? (espresso/latte/cappuccino):").lower()).replace(' ','')

    if user_choice == "off":
        is_on = False
        break
    if user_choice == "report":
        print("resources is:\n")
        print(f'water: {resources["water"]}')
        print(f'milk: {resources["milk"]}')
        print(f'coffe: {resources["coffee"]}')
        print(f'Money: ${profit}')

    #TODO: 2. Check resource sufficient ?
    #Helper

    def check_resource(item):
        if resources["water"] < MENU[item]["ingredients"]["water"]:
            return "Sorry there is not enough water."
        elif resources["milk"] < MENU[item]["ingredients"]["milk"]:
            return "Sorry there is not enough milk."
        elif resources["coffee"] < MENU[item]["ingredients"]["coffee"]:
            return "Sorry there is not enough coffee."
        else:
            return True


    #TODO: 3. Process coin

    def insert_coins():
        print("Please insert coins\n")
        quarters = int(input("How many quarters?:"))
        dimes = int(input("How many dimes?:"))
        nickles = int(input("How many nickles?:"))
        pennies = int(input("How many pennies?:"))
        pocket = {
            'quarters' : quarters,
            'dimes' : dimes,
            'nickles' : nickles,
            'pennies' : pennies
        }
        return pocket
    def calculate(q,d,n,p):
        calculation = (q * 0.25) + ( d * 0.10) + (n * 0.05) + (p *0.01)
        return round(calculation,2)

    user_coins = insert_coins()
    user_money = calculate(user_coins['quarters'],user_coins['dimes'],user_coins['nickles'],user_coins['pennies'])


    #TODO: 4. Check transaction successful ?
    if user_money < MENU[user_choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        profit = profit + MENU[user_choice]["cost"]
        change = round((user_money - profit),2)
        print(f'proif is: {profit}')

    #TODO: 5. Make coffe
    resources["water"] -=MENU[user_choice]["ingredients"]["water"]
    resources["coffee"] -=MENU[user_choice]["ingredients"]["coffee"]
    if user_choice != "espresso":
        resources["milk"] -=MENU[user_choice]["ingredients"]["milk"]

    print(f'Here is your ☕ {user_choice}. Enjoy!')
