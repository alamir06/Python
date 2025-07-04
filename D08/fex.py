import math

def calc_paint(height,width,covearge):
    calc=(height*width)/coverage
    calc=math.ceil(calc)
    print(f"you'll need {calc} paint of cans")

height=int(input("Enter the hiedght of you wall?:"))
width=int(input("enter the width of your wall?:"))
coverage=5
calc_paint(height=height,width=width,covearge=coverage)


