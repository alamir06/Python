# calculator
from art import logo
import os
# addition
def add(n1,n2):
    return n1 + n2
# subtraction
def subtract(n1,n2):
    return n1 - n2
# multiplication
def multiply(n1,n2):
    return n1 * n2
# division
def devide(n1,n2):
    return n1 /  n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":devide
}
def calculator():
    print(logo)
    n1=float(input("What is the first number?:"))
    for operator in operations:
        print(operator)
    should_continue=True
    while should_continue:
        operationSymbol=input("Pick the operation!:")
        n2=float(input("What is the next number?:"))
        calculation_function=operations[operationSymbol]
        result=calculation_function(n1=n1,n2=n2)
        print(f"{n1} {operationSymbol} {n2}={result}")
        if input(f'Type "y" for continue operation with the {result} or "n" to start new opeartion!:')=="y":
            n1=result
        else:
            should_continue=False
            os.system('cls')
            calculator()
calculator()