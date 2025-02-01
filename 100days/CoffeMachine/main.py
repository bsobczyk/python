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




#TODO: 1. Print request_port
user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()

#TODO: 2. Check resource sufficient ?
#Helper
print("resources is:\n")
print(f'water: {resources["water"]}')
print(f'milk: {resources["milk"]}')
print(f'coffe: {resources["coffee"]}')

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
print("Please insert coins\n")
quarters = int(input("How many quarters?:"))
dimes = int(input("How many dimes?:"))
nickles = int(input("How many nickles?:"))
pennies = int(input("How many pennies?:"))
def calculate(q,d,n,p):
    calculation = (q * 0.25) + ( d * 0.10) + (n * 0.05) + (p *0.01)
    return round(calculation,2


print(calculate(quarters,dimes,nickles,pennies))
#TODO: 4. Check transaction successful ?
#TODO: 5. Make coffe

