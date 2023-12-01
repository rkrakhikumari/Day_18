MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

profit = 0
resources ={
    "water": 300,
    "milk": 200,
    "coffee": 100,

}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    print("please insert coins")
    total = int(input("how many five: ")) * 5
    total += int(input("how many ten: ")) * 10
    total += int(input("how many twenty: ")) * 20
    total += int(input("how many fifty: ")) * 50
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is Rs{change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. money refunded")
        return False
    
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}. Enjoy!!!")

is_on = True

while True:
    choice = input("What would you like? espresso/latte/cappuccino: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
       print(f"water: {resources['water']}ml")
       print(f"milk: {resources['milk']}ml")
       print(f"coffee: {resources['coffee']}g")
       print(f"money: {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
        if is_transaction_successful(payment, drink["cost"]):
            make_coffee(choice,drink["ingredients"])
