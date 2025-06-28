# problem , calculate the BMI
weight=float(input("Enter your weight in kg: "))

height=float(input("Enter your height in meters: "))
# Calculate BMI
bmi = weight / (height ** 2) 

print("Your BMI is: ", bmi)
 
# The code calculates the Body Mass Index (BMI) based on user input for weight and height.
# It then categorizes the BMI into different weight status categories.
# The categories are underweight, normal weight, overweight, and three classes of obesity.
# The program uses conditional statements to determine the appropriate category based on the calculated BMI.