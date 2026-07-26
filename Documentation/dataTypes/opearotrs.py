# Operators
''' Arithmetic Operators
+ : Addition
- : Subtaraction
* : Multiplication
/ : Exponential
% : Modulo
// : Floor division
'''
# Simple calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
inp = input("Enter what u want to do: ")

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

if inp == '+':
    print(add(a,b))
elif inp == '-':
    print(sub(a,b));
elif inp == '*':
    print(mul(a,b))
elif inp == '/':
    print(div(a,b))
else:
    print("Please enter a valid choice !")