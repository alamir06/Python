# rock ,paper,scissors
rock ='''
    _______
    ---'   ____)
    _______)
    _______)        
    _______)
    _______)
    ---'   ____)
    '''

paper = '''
    _______
    ---'   ____)
    _______)    
    _______)
    _______)
    _______)
    ---'   ____)
    '''
scissors = '''
    _______
    ---'   ____)
    _______)        
    _______)
    _______)
    _______)
    ---'   ____)
    '''
list_of_choices = [rock, paper, scissors]
computer_choice = 0
user_choice = 0
import random
print("Welcome to Rock, Paper, Scissors!")
print("Choose your weapon:\n 0: Rock \n 1: Paper \n 2: Scissors")
user_choice = int(input("Enter your choice (0, 1, or 2): "))
computer_choice = random.randint(0, 2)
print(f"You chose:\n{list_of_choices[user_choice]}")
print(f"Computer chose:\n{list_of_choices[computer_choice]}")
if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")
# End of the rock, paper, scissors game
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
print(fruits)
fruits.count('tangerine')
print(fruits)

fruits.index('banana')
print(fruits)
fruits.index('banana', 4)  # Find next banana starting at position 4
print(fruits)
fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

fruits.pop()