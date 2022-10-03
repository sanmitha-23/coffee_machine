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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_sufficient(order_ingredients):
    """Returns true if coffee can be made, else returns false"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, no sufficient {item}")
            return False
    return True


def process_coins():
    """Returns the total calculated money after an order"""
    print("Please insert your coins")
    quarters = int(input("Enter the number of quarters: ")) * 0.25
    dimes = int(input("Enter the number of dimes: ")) * 0.10
    nickles = int(input("Enter the number of nickles: ")) * 0.05
    pennies = int(input("Enter the number of pennies: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def is_money_sufficient(money_received,cost):
    if money_received >= cost:
        change = round(money_received - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")


def make_coffee(order_ingredients, drink_name):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕. Enjoy!!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_money_sufficient(payment, drink['cost']):
                make_coffee(drink['ingredients'], choice)
