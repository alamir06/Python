# control flow:means of controlling the flow of execution in a program.
# if, else, elif, for, while, break, continue, pass ,loop, range, etc.
# if statement :excute a block of code if a condition is true.
# if condition:
#     # code to execute if condition is true
# else:
#     # code to execute if condition is false
# # if-else statement: execute one block of code if a condition is true, and another block if it is false.
# if condition1:
#     # code to execute if condition1 is true
# elif condition2:
#     # code to execute if condition2 is true
# else:
#     # code to execute if both conditions are false
# e.g.
age = int(input("Enter your age: "))
if age<18:
    print("You are a small, you can not elect the prime ministr.")
elif age>= 18 and age < 60:
    print("You are on required age  and you can elect the prime ministr.")
else:
    print("You are a not eligible for election.")
# e.g.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"number {number} is even.")
else:
    print(f"number { number} is odd.")