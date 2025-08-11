from art import logo
print(logo)

name=input("Whar is your name:")
print(f"Hello {name} Wellcome to Number Guessing Game!") 
import random
alice=random.randint(1,100)

def check_answer(guess,answer,turns):
    if guess>answer:
        print("Too high")
        return turns-1
    elif guess<answer:
        print("Too low")
        return turns-1
    else:
        print(f"congrats 🙏You Got it!!!, The number was {alice}.")
        

def chech_difficulty():
    difficulty=input("enter level of the game, hard or easy!").lower()
    if difficulty=="hard":
        return 5
    elif difficulty=="easy":
        return 10
    else:
        print("Invalid level of the game, Please enter the correct evel of the Game!")


turns =chech_difficulty()
guess=0

while guess!=alice:
    print(f"you have {turns} remaining chance!")
    guess=int(input("Guess the Number:"))
    turns=check_answer(guess,alice,turns)
    if turns==0:
        print("you have no more chnace left, you lose!")
        print("Play again!")
        play_again=input(f"do yo want to play again? yes or no")
        if play_again.lower() == 'yes':
            alice = random.randint(1, 100)
            turns = chech_difficulty()
            guess = 0
        else:
            print("Thanks for playing!")
    if guess == alice:
        play_again = input(f"do yo want to play again? yes or no")
        if play_again.lower() == 'yes':
            alice = random.randint(1, 100)
            turns = chech_difficulty()
            guess = 0
        else:
            print("Thanks for playing!")
            break



