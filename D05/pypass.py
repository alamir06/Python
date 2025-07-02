import random
capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
special_characters = ['!','@','#','$','%','^','&','*','(',')','-','=','+']
small_letters=['a,b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# total_cahr=[capital_letters, numbers, special_characters, small_letters]

# print("Welcome to the Password Generator!")
# length = int(input("How many characters do you want in your password? "))
# password = []
# for i in range(length):
#     password.append(random.choice(random.choice(total_cahr)))
# print("Your password is: ", ''.join(password))

capital_selection = int(input("How many capital letters do you want in your password? "))
number_selection = int(input("How many numbers do you want in your password? "))
special_selection = int(input("How many special characters do you want in your password? "))
small_selection = int(input("How many small letters do you want in your password? "))
password = []


for i in range(capital_selection):
    password.append(random.choice(capital_letters))

for i in range(number_selection):
    password.append(random.choice(numbers))         

for i in range(special_selection):
    password.append(random.choice(special_characters))

for i in range(small_selection):
    password.append(random.choice(small_letters))

for i in range(len(password)):
    random.shuffle(password)

nw_pass= ''.join(password)
print("Your password is: ",nw_pass)


