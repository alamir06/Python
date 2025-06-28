# this is number manipulation module
# round a number to the nearest integer
# sytax: round_number(number)
# example: round_number(3.6) returns 4
# example: round_number(3.66666,3) returns 3.67

# problem:calculate life of weeks 
age=int(input("Enter your age: "))
left_years=90-age
weeks=left_years*52
print(f"You have {weeks} weeks left to live.")