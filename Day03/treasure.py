# 
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("Which direction do you want to go? Type 'left' or 'right': ").lower()
if direction == "left":
    transport = input("You come to a river. Do you want to swim or wait for a boat? Type 'swim' or 'wait': ").lower()
    if transport == "wait":
        door = input("You arrive at a house with three doors. Do you want to open the red, blue, or yellow door? Type 'red', 'blue', or 'yellow': ").lower()
        if door == "yellow":
            print("You found the treasure! You win!")
        elif door == "blue":
            print("You enter a room full of beasts. Game over.")
        elif door == "red":
            print("You were burned by fire. Game over.")
        else:
            print("You chose a door that doesn't exist. Game over.")
    elif transport == "swim":
        print("You were attacked by a shark. Game over.")
else:
    print("You fell into a hole. Game over.")
# end of the code