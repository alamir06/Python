import random
emoji=["😁","😁😁","😁😁😁","😁😁😁😁","😁😁😁😁😁","😁😁😁😁😁😁"]
num=int(input("Enter a number from 0 to 3. pls dont pick any other number: "))
if 0<=num<4:
    print('good')
    computer=random.randint(0,3)
    print(computer)
    sum=num+computer
    print(sum)
else:
    print('pick another number')
list=[]
list.append(emoji[sum])
print(list)