# variable is a memory location used to store avlue for later use
# variable is a name given to a memory location that stores a value
# variabale is a phonebook name real world example
name="Alamirew Wagaw"
print(name)
name="Aklilu Wagaw"
print(name)
name=input("Whatb is your name? ")
length=len(name)
print("Hello, " + name + "! Your name has " + str(length) + " characters.")

# variable to swapping the value of two variables
a=input("Enter the first number: ")
b=input("Enter the second number:")

print("Before swapping: a =", a, ", b =", b)
c=a
a=b
b=c
print("After swapping: a =", a, ", b =", b)
