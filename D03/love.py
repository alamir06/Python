# love calculator
name1 = input("Enter your name: ")
name2 = input("Enter your crush's name: ")
name1=name1.lower()
name2=name2.lower()
# count the number of letters in both names
t=name1.count("t")
print("t:", t)
r=name1.count("r")
print("r:", r)
u=name1.count("u")
print("u:", u)
e=name1.count("e")
print("e:", e)
# count the number of letters in the word "true"
treue_cout=t+r+u+e
print("treue_cout:", treue_cout)
l=name1.count("l")
print("l:", l)
o=name1.count("o")
print("o:", o)
v=name1.count("v")
print("v:", v)
e=name1.count("e")
print("e:", e)

# count the number of letters in the word "love"
love_count=l+o+v+e
print("love_count:", love_count)

# calculate the love score
love_score = str(treue_cout) + str(love_count)
# love_count=int(treue_cout) + int(love_count) # do not use this line because it will convert the score to an integer
print("Your love score is: " + love_score)
print("Your love score is: " + str(love_count))
# check the love score
if int(love_score) < 10 or int(love_score) > 90:
    print("You go together like coke and mentos.")
elif 40 <= int(love_score) <= 50:
    print("You are alright together.")
else:
    print("Your score is " + love_score + ".")
    print("You are not bad together.")
# end of the code
