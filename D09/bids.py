from logo import logo
import os

print("A System that used to calculate the wins Bids!!!: ")
bids_dictionary={}
def add_bids(name,bids):
    bids_dictionary[name]=bids
    print(bids_dictionary)


def askfu():
    name=input("What is your name?")
    bids=int(input("Enter your bids?:$ "))
    add_bids(name=name,bids=bids)
    another_bids=input("Do you want another bids? yes/no:")
    if another_bids=="yes":
        os.system('cls')
        askfu()
    elif another_bids=="no":
        for bid in bids_dictionary:
            max_bid=0
            # print(bids_dictionary[bid] )
            if bids_dictionary[bid] > max_bid:
                max_bid=bids_dictionary[bid]   
        print(max_bid)
    else:
        print("Please enter the correct feature!")
askfu()
# print(max_bid)
