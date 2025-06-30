total=0
for  n in range(1, 101):
    total += n
print("Total sum from 1 to 100 is:", total)

number=int(input("Enter a number: "))
sum=0
for i in range(1, number + 1):
    if i % 2 == 0:
        sum += i
print("Sum of even numbers from 1 to", number, "is:", sum)
