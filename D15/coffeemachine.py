# this is a code to coffee machine
from data import MENU,resources

profit=0

def report_function():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")

def is_resources_sufficient(drink):
    for item in drink["ingredients"]:
        if drink["ingredients"][item]>=resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True

def is_payement():
    print("Please insert coins.")
    total=int(input("how many quarters?: "))*0.25
    total+=int(input("how many dimes?: "))*0.10
    total+=int(input("how many nickles?: "))*0.05
    total+=int(input("how many pennies?: "))*0.01
    return total

def is_transaction_successful(money_received,drink_cost):
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def is_resources(drink):
    for item in drink["ingredients"]:
        resources[item]-=drink["ingredients"][item]
    print(f"Here is your {user_input} ☕️. Enjoy!")


is_coffe=True
while is_coffe:
    user_input=input("What do you want? (espresso/latte/cappuccino): ")
    if user_input=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
    elif user_input=="off":
        is_coffe=False
    else:
        check=["espresso","latte","cappuccino"]
        if user_input in check:
            drink=MENU[user_input]
            if is_resources_sufficient(drink):
                process= is_payement()
                if is_transaction_successful(process,drink["cost"]):
                    is_resources(drink)
        else:
            print("Invalid input")
# this is a code to coffee machine

        

