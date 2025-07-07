from logo import logo
import os

print("A System that used to calculate the wins Bids!!!: ")
bids_dictionary={}
def add_bids(name,bids):
    bids_dictionary[name]=bids

continue_add=True
while continue_add:
    name=input("What is your name?")
    bids=int(input("Enter your bids?:$ "))
    add_bids(name=name,bids=bids)

    another_bids=input("Do you want another bids? yes/no:")
    if another_bids=="yes":
        os.system('cls')
    elif another_bids=="no":
        continue_add =False
max_bid=0
winner=''
for bidder in bids_dictionary:
    if bids_dictionary[bidder]>max_bid:
        max_bid=bids_dictionary[bidder]
        winner=bidder
print(f"The winner is {winner} with the bids of{max_bid}!")