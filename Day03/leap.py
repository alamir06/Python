# leap year checker
# leap year is a year that have 366 days instead of the usual 365 days
# a leap year occurs every 4 years, except for end-of-century years. 
# The year can be a leap year if it is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
# For example, the year 2000 was a leap year, but 1900 was not.
# Solution 1:
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")    
else:
    print(f"{year} is not a leap year.")
# Example usage:
# Enter a year: 2000
# 2000 is a leap year.
# Solution 2:
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")