# BMI interpretor
weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in m: "))
BMI=weight/height ** 2
if BMI < 18.5:
    print("You are underweight.")
elif 18.5 <= BMI < 24.9:
    print("You are normal weight.")
elif 25 <= BMI < 29.9:
    print("You are overweight.")    
elif 30 <= BMI < 34.9:
    print("You are obese (Class 1).")
elif 35 <= BMI < 39.9:
    print("You are obese (Class 2).")
else:
    print("You are obese (Class 3).")   
print("Your BMI is:", round(BMI, 2))
# This code calculates the Body Mass Index (BMI) based on user input for weight and height,
# and categorizes the BMI into different health classifications.