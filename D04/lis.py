# list is a collection of items in a particular order
# list is mutable, meaning we can change its content
# list is defined by square brackets
# list is iterable, meaning we can loop through it
# list is a  data structure that can hold multiple items with different data types
# e.g. list = [1, 2, 3, 4, 5,"string", True, 3.14]
names=[]
for i in range(5):
    name = input("Enter a name: ")
    names.append(name)
# import random module to choose a random name
import random
# print the list
print(names)
random_name=random.choice(names)
# print the random name
print(f"{random_name} will but todays meal!")
