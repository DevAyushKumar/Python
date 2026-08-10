#Python Class Meathods
'''Python Class Meathods: An introduction
-> IN Python, classes are a way to define custom data types that can store data and define functions that can manipulate that data. One type of function that can be defined within a class is called a "meathod". In this blog post, we will explore what python class meatods are, why they are useful and how to use them.

What are python class meathods ?
-> A class meathod is a type of meathod that is bound to the class not the inheritance of the class. In other words, it operates on the class as a whole, rather than on a specific instance of the class. Class meathods are defined using the "@classmeathod" decorator, followed by a function defination. The first argument of the function is always "cls", which represents the class itself. 

Why use python class meathods ?
-> Class meathods are useful in several situations. For example, you might want to create a factory meathod that creates an instance and returns it to the caller. Another common use case is to provide alternative constructors for your class. This can be useful if you want to create instances of your class in multiple ways, but still have a consistent interface for doing so.'''
class ExampleClass:
    @classmeathod
    def factory_meathod(cls, argument1, argument2):
        return clr(argument1, argument2)
'''In this example, the "factory_meathod" is a clss meathod that takes two arguments, argument1 and argument2. It creates a new instance of the classs "ExampleClass" using the "cls" keyword, and returns the new isntance to the caller.'''