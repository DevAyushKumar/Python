a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

inp = input("Enter the function you want to do: ")
if inp == '+':
    print(add(a,b))
elif inp == '-':
    print(sub(a,b))
elif inp == '*':
    print(mul(a,b))
elif inp == '/':
    print(div(a,b))
else:
    print('Enter a valid choice')