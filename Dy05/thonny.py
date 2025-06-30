# from me
names=['alamirew',"aklilu","GHN","Temesgen","bimrew", "bruk"]
print("There are", len(names), f"names in the list. which are:{names} wahat name do you want to search for?")
user_choice = input("Enter the name you want to search for: ")
import random
computer_choice = random.choice(names)
if user_choice == computer_choice:
    print(f"You win! The name you chose is the same as the computer's choice.{user_choice} == {computer_choice}")
else:
    print("You lose! The name you chose is not the same as the computer's choice.")
    print(f"Your choice: {user_choice}, Computer's choice: {computer_choice}")

name1=input("Enter the first name: ")
name2=input("Enter the second name: ")
name1=name1.lower()
name2=name2.lower()
true_count=name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
love_count=name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")
love_count = str(love_count) + str(true_count)
print(f"Your love score is: {love_count} %")
