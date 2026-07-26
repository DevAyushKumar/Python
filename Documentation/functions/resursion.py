'''Recursion in python:
Recursion is the process of defining somethin in the term of itself.
A physical world example would be to place two parallel mirrors facing each other. Any object in between them would be reflected recursively.

Python recursive function:
In python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as reccursive functions.'''
def factorial(num):
    if(num==1 or num==0):
        return 1
    else:
        return num*factorial(num-1)
num = 3
print(factorial(num))