# debugging is the proccess of finding and fixing bugs or errors  in code.
# debugging is an essential skill for programmers to master.
# it involves systematically testing and analyzing code to identify issues.
# debugging can be done using various tools and techniques, such as print statements, debuggers, and logging.
# common debugging techniques include:
# 1. print statements: inserting print statements to check variable values and program flow.
# 2. debuggers: using integrated development environment (IDE) debuggers to step through code.
# 3. logging: writing logs to track program execution and errors.
# 4. unit tests: creating tests to verify code functionality and catch bugs early.
# 5. code reviews: having peers review code to catch potential issues.
# effective debugging requires patience, attention to detail, and a systematic approach.
# there are best ideas for debugging, such as:
# #1. Define the problem clearly: understand what the code is supposed to do and what it is doing instead.
# def my_function():
#     for i in range(1,20):
#         if i==20:
#             print("i is 20")
# my_function()
# solution: the loop should run until 20, but it stops at 19. Change the range to (1, 21).

# # 2. Reproduce the issue: ensure you can consistently reproduce the bug.
# from random import randint
# diceImgs=['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣']
# randNum=randint(1,6)# this generates a random number between 1 and 6 so you have to use randint(0-5)
# print(diceImgs[randNum])

# solution: the random number generation is correct, but ensure the diceImgs list is indexed correctly.

# #  3. Isolate the problem: narrow down the code to the smallest section that causes the issue.
# #  e.g: play computer
# year=int(input("Enter the Your Birth year: "))
# if year>1980 and year<1994:
#     print("You are a millennial.")
# elif year >1994:# this should be year >= 1994 to include 1994 in Gen Z
#     print("You are a Gen Z.")

# solution: the code correctly identifies millennials and Gen Z, but ensure the input is valid and handle edge cases. e.g. if the input is not a number or is out of range. and 1994 is not included in the Gen Z range.

# # 4. Check for common errors: look for syntax errors, typos, and logical mistakes. and fix it especially at typeError line
# age=input("Enter your age: ")
# if age < 18:
#     print("You are a minor {age}.")

# solution: the input is a string, so it should be converted to an integer before comparison. Use `int(age)` to fix the type error.

# # use print statements to check variable values and program flow. it is my best friend when debugging.
# pages=0
# words_per_page=0
# pages=int(input("Enter the number of pages: "))
# words_per_page==int(input("Enter the number of words per page: "))
# print(f"Number of pages: {pages}")
# print(f"Words per page: {words_per_page}")
# total_words=pages*words_per_page
# print(f"Total words in the book: {total_words}")

# # solution: the code has a typo in the second input line where `==` should be `=`. Change it to `words_per_page = int(input("Enter the number of words per page: "))`.


# debuggers are powerful tools that allow you to step through code, inspect variables, and evaluate expressions in real-time.
# def listMutation(first_list):
#     mutate_list=[]
#     for i in first_list:
#         new_item=i*2
#     mutate_list.append(new_item)
#     print(mutate_list)

# listMutation([1, 2, 3, 4, 5])
# solution: the code has a logical error where `new_item` is not being added to `mutate_list` inside the loop. It should be `mutate_list.append(new_item)` inside the loop to collect all mutated items.

# 5. Use version control: track changes to code and revert to previous versions if necessary.
# 6. Take breaks: stepping away from the code can provide fresh perspectives.
# 7. Document findings: keep notes on what worked and what didn't for future reference.
# mastering debugging takes practice, but it is a valuable skill that improves coding efficiency and quality.


# Exercise:
