
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee beans": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee beans": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee beans": 24,
        },
        "cost": 3.0,
    }
}


def report(resource_list):
    print(resource_list)


resources = {
    "water": 750,
    "milk": 400,
    "coffee beans": 100,
}
profit = 0


def check_resource(res, menu):
    for item in menu:
        if menu[item] > res[item]:
            print(f"Sorry, coffee can not be made.\nPlease refill {item}.\n")
            return False
    return True


def money_check(money, menu):
    change = money - menu["cost"]
    return change


def resources_left(res, menu):
    for x in res:
        res[x] -= menu[x]
    return res


on = True
while on:
    coffee_possible = True
    coffee = input("What kind of coffee would you like to have? espresso, latte, or cappuccino:  ").lower()
    if coffee == "off":
        on = False
    elif coffee == "report":
        print(f"\nWater: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee beans: {resources["coffee beans"]}g\nMoney: ${round(profit, 2)}\n")
    else:
        coffee_possible = check_resource(resources, MENU[coffee]["ingredients"])
        if coffee_possible:
            print("Please insert coins.")
            quarters = float(int(input("Enter quarters:  ")) * 0.25)
            dimes = float(int(input("Enter dimes:  ")) * 0.1)
            nickels = float(int(input("Enter nickels:  ")) * 0.05)
            pennies = float(int(input("Enter pennies:  ")) * 0.01)
            money = quarters + dimes + nickels + pennies
            change = money_check(money, MENU[coffee])
            if change >= 0:
                profit += (money - change)
                print(f"Here is your change:  ${round(change, 2)}")
                print(f"Here is your {coffee} ☕\n")
                resources_update = resources_left(resources, MENU[coffee]["ingredients"])
                resources = resources_update
            else:
                print("Sorry, you don't have enough money.\nPayment refunded.\n")







