def prime_checker(number):
    if number < 0:
        print("Negative numbers do not have a property of primality!")
    elif number in (0, 1):
        print(f"Number {number} is neither prime nor composite!")
    else:
        for i in range(2, int(number ** 0.5) + 1):  # Optimized range
            if number % i == 0:
                print(f"Number {number} is a composite number!")
                break
        else:
            print(f"Number {number} is a prime number!")


number = int(input("Enter the number you want to check for primality: "))
prime_checker(number)
