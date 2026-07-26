'''Docstrings in python:
Python docstrings are the string literals that appear right after the defination of a function, meathod, class or module'''
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
'''Here in a number n, returns the square of n'''#is the docstring which will not appear in the output

#Python comments vs docstrings
'''Python Comments:
Comments are descriptions that help programmers better understand the intent and functionalilty of the program. They are completely ignored by the Python interpreter.

Python docstrings:
As mentioned above, python docstrings are strings used right after the defination of a function, meathod, class or module (like in example 1). They are used to document our code.
We can access these docstrings using the doc attribute

Python doc attribute:
Whenever strings literals are present just after the defination of a function, module, class or meathod, they are associated with the object as their doc attribute. We can later use this attribute to retrive this docstring'''
def square(n):
    '''Takes in number n, and returns the square of n'''
    print(n**2)
print(square.__doc__)

'''PEP 8:
PEP 8 is a document that provides guidlines and best practice on how to write python code. It was written in 2001 by Guide van Rossum, Barry Warsaw and Nick Coghian. The primary focus of PEP 8 is to improve the readability and consistency of python code. 
PEP stands for Python Enhancement Proposal and there are several of them. A PEP is a document that describes new features proposed for python and documents aspects of python, like design and style for the community.'''
