resources = {"Water": 9000, "Milk": 48000, "Coffee": 2100, "Money": 0}

recipe = {
    "Espresso": {"Water": 30, "Milk": 0, "Coffee": 7, "Money": 2.00},
    "Latte": {"Water": 30, "Milk": 240, "Coffee": 7, "Money": 4.00},
    "Cappuccino": {"Water": 30, "Milk": 120, "Coffee": 7, "Money": 3.50},
}

coins = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}


def insert_coins(price):
    inserted_money = 0
    for i in coins:
        inserted_money += int(input(f"How many {i} ")) * coins[i]

    if inserted_money < price:
        print("Sorry that's not enough money. Money refunded.")
        return False

    resources["Money"] += price
    print(f"Here is ${round(inserted_money-price,2)} dollars in change.")
    return True


def process(choice):
    for i in recipe[choice]:
        if i == "Money":
            return insert_coins(recipe[choice][i])
        elif resources[i] < recipe[choice][i]:
            print(f"Sorry there is not enough {i.lower()}.")
            break
        else:
            resources[i] -= recipe[choice][i]
    return False


run = True

while run:
    choice = input("What would you like? (espresso/latte/cappuccino): ").title()

    if choice == "Off":
        run = False
    elif choice == "Report":
        for key, value in resources.items():
            print(f"{key}: {value}")
    elif choice in recipe:
        if process(choice) == True:
            print(f"Here is your {choice}. Enjoy!")
