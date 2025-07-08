def is_leep(year):
    if year%4==0:
        if year % 100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    dayofMonth=[31,28,31,30,31,30,31,31,30,31,30,31]
    if month==2 and is_leep(year):
        return 29
    else:
        return dayofMonth[month - 1]


# asking part
year=int(input("Enter The Year!:"))
month=int(input("Enter the month!:"))
days=days_in_month(year=year,month=month)
print(days)