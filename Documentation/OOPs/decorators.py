'''python decorators:
Python decorators are a powerful and versetile tool that allows you to modify the behaviour of function and meathods. They are a way to extend the functionality of a function or meathod without modifying its source code.
A decorator is a function that takes another function as an argument and returns a new function taht modifies the behaviour of the original function. The new function if ofter refered to as decorator function. The basic syntax for using the decerator is the following.'''
def greet(fx):
    print("good morning")
    fx()
    print("thanks for using our program")

@greet
def hello():
    print("Hello")
'''Decorators are often used to add functionality to functions and meathods, such as logging, momorizing and access control.'''

'''Conculsion:
Decorators are a powerful and flexiable feature in Python that can be used to add functionality to functions and meathods without modfying their source code. They are great tool for seperating concerns, reducing code deuplication and making your code more readable and maintainable.

In conclusion, python decorators are a way to extend the functionality of functions and meathods, by modifying its behaviour without modifying the source code. They are used for a variety of purposes, such as logging, moemoization, access control and more. They are a powerful tool that can be used to make your code more readable, maintainable and extendable.'''