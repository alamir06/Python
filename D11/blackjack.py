# Blakjack Game
import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
userScore=[]
computerScore=[]
for i in range(0,2):
    userrandom=random.randint(1,11)
    userScore.append(cards[userrandom])
    computerrandom=random.randint(1,11)
    computerScore.append(cards[computerrandom])

print(userScore)
print(computerScore)
userSum=0
computerSum=0
for i in range(2):
    userSum+=userScore[i]
    computerSum+=computerScore[i]

# print(userSum)
# print(computerSum)
