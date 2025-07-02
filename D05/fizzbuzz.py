fizz_end_number=int(input("Enter the end number for FizzBuzz: "))
for i in range(1, fizz_end_number + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz",end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
# This code implements the FizzBuzz problem, where it prints "Fizz" for multiples of 3,