'''Functions:
A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amount of code, it is advisable to create of use existing function that make the program floe organized and neat.
There are two types of functions:
1. Built in functions
2. user defined functions

Built in Functions:
These functions are defined and pre coded in python. Some examples of built in function as follows:
min(), max(), len(), sum(), type(), range(), print(), etc.

User defined functions:
We can create functions to perform specific tasks as per our needs. Such functions are called user defined functions.'''
def function_name(parameters):
    pass
    #code and statement

'''
* Create a function using the def keyword, followed by a function name, followed by a paranthesis (0) and colon(:).
* Any parameters and arguments should be placed within the paranthesis.
* Rules to naming function are similar to that of naming variables.
* Any statemnets and other code within the function should be indented.

Calling a function:
We call a functions by giving the function name, followed by parameters (if any) in the paranthsis.'''
def name(fname, lname):
    print("Hello", fname, lname)
name("Ayush","Kumar")