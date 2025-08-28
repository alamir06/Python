# this is a code to coffee machine
from data import MENU,resources
user_input=input("What do you want? (espresso/latte/cappuccino): ")
coffe=True
while coffe:
    if user_input=="report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
    elif user_input=="espresso":
        if resources['water']<MENU['espresso']['ingredients']['water']:
            print("Sorry there is not enough water.")
        elif resources['coffee']<MENU['espresso']['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
        else:
            resources['water']-=MENU['espresso']['ingredients']['water']
            resources['coffee']-=MENU['espresso']['ingredients']['coffee']
        print("Please enter the coins below")
        quarters=int(input("How many quarters?: "))
        dimes=int(input("How many dimes?: "))
        nickels=int(input("How many nickels?: "))
        pennies=int(input("How many pennies?: "))
        total=quarters*0.25+dimes*0.1+nickels*0.05+pennies*0.01
        if total<MENU['espresso']['cost']:
            print("Sorry that's not enough money. Money refunded.")
            resources['water']+=MENU['espresso']['ingredients']['water']
            resources['coffee']+=MENU['espresso']['ingredients']['coffee']
        else:
            change=round(total-MENU['espresso']['cost'],2)
            if change>0:
                print(f"Here is ${change} in change.")
        print("and enjoy with your espresso!☕️")
    elif user_input=="latte":
        if resources['water']<MENU['latte']['ingredients']['water']:
            print("Sorry there is not enough water.")
        elif resources['milk']<MENU['latte']['ingredients']['milk']:
            print("Sorry there is not enough milk.")
        elif resources['coffee']<MENU['latte']['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
        else:
            resources['water']-=MENU['latte']['ingredients']['water']
            resources['milk']-=MENU['latte']['ingredients']['milk']
            resources['coffee']-=MENU['latte']['ingredients']['coffee']
        print("Please enter the coins below")
        quarters=int(input("How many quarters?: "))
        dimes=int(input("How many dimes?: "))
        nickels=int(input("How many nickels?: "))
        pennies=int(input("How many pennies?: "))
        total=quarters*0.25+dimes*0.1+nickels*0.05+pennies*0.01
        if total<MENU['latte']['cost']:
            print("Sorry that's not enough money. Money refunded.")
            resources['water']+=MENU['latte']['ingredients']['water']
            resources['milk']+=MENU['latte']['ingredients']['milk']
            resources['coffee']+=MENU['latte']['ingredients']['coffee']
        else:
            change=round(total-MENU['latte']['cost'],2)
            if change>0:
                print(f"Here is ${change} in change.")
        print("and enjoy with your latte ☕️")
    elif user_input=="cappuccino":
        if resources['water']<MENU['cappuccino']['ingredients']['water']:
            print("Sorry there is not enough water.")
        elif resources['milk']<MENU['cappuccino']['ingredients']['milk']:
            print("Sorry there is not enough milk.")
        elif resources['coffee']<MENU['cappuccino']['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
        else:
            resources['water']-=MENU['cappuccino']['ingredients']['water']
            resources['milk']-=MENU['cappuccino']['ingredients']['milk']
            resources['coffee']-=MENU['cappuccino']['ingredients']['coffee']
        print("Please enter the coins below")
        quarters=int(input("How many quarters?: "))
        dimes=int(input("How many dimes?: "))
        nickels=int(input("How many nickels?: "))
        pennies=int(input("How many pennies?: "))
        total=quarters*0.25+dimes*0.1+nickels*0.05+pennies*0.01
        if total<MENU['cappuccino']['cost']:
            print("Sorry that's not enough money. Money refunded.")
            resources['water']+=MENU['cappuccino']['ingredients']['water']
            resources['milk']+=MENU['cappuccino']['ingredients']['milk']
            resources['coffee']+=MENU['cappuccino']['ingredients']['coffee']
        else:
            change=round(total-MENU['cappuccino']['cost'],2)
            if change>0:
                print(f"Here is ${change} in change.")
        print("and enjoy with your cappuccino ☕️")
    elif user_input=="off":
        coffe=False
    else:
        print("Invalid input")
