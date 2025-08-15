from art import logo,vs
from data import data
import random

score=0
Is_true=True

def check_answer(question,randomA,randomB):
        global score, Is_true
        if question=="A":
            if randomA["followers"]>=randomB["followers"]:
                score+=1
            else:
                 Is_true=False
        elif question=="B":
            if randomB["followers"]>=randomA["followers"]:
                    score+=1
            else:
                     Is_true=False
        else:
                print("Please enter the correct Question?")
      
while Is_true:
        randomA=random.choice(data)
        randomB=random.choice(data)
        if randomA==randomB:
              randomB=random.choice(data)
        print(f"Score={score}")
        print(logo)
        print(f'Compare A :{randomA["name"]},{randomA["job"]}, from {randomA["country"]}')
        print(vs)
        print(f'Against B :{randomB["name"]},{randomB["job"]}, from {randomB["country"]}')
        question=input("Which has More Followers? A or B:")
        check_answer(question,randomA,randomB)
        
print(f"Your Score ={score}")


