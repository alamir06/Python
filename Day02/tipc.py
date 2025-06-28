# problem for develp tip calculator
bill=float(input("Enter the total bill amount: $"))
tip=int(input("Enter the tip percentage : 12,10,15,20: "))
person=int(input("Enter the number of people to split the bill: "))
tip_amount= (tip/100)*bill
total_bill = bill + tip_amount
per_person = total_bill / person
# total_bill = (bill + ((tip / 100) * bill)) / person #more optimize
print(f"Total bill amount: ${total_bill:.2f}")
print("for each person to pay: $", per_person)
