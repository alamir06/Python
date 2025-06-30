# about randomization in python
# randomization is the process of making something random or unpredictable values Based on a range or a set of values
# it is often used in games, simulations, and other applications where unpredictability is desired
# to do it we import random module
# module means some document or prepared value to do a specific task or more than task
import random
random_integer=random.randint(1,10)
# print(random_integer)
random_float=random.random()
# print(random_float)

HT_game_level=random.randint(0,1)
# print(HT_game_level)
if HT_game_level== 0:
    print("Heads")
else:
    print("Tails")
# random.choice() is used to select a random element from a list