'''Single Inheritance in Python:
Single inheritance is a type of inheritance when a class inherits properties and behaviours from a singlr parent class. This is the simplest and most common form of inheritance.

Synatx:
The synatx for single inheritance in Python is straightforward and easy to understand. To create a new class that inherits from a parent class, simply specify the parent class in the class defination, inside the parentheses, like this'''
class Childclass(parentClass):
    def __init__(self):
        pass

'''Example:
Let's consider a single experience of single inheritance in Python. Consider a class named "Animal" that contains the attributes and behanviours that are common in animals.'''
class animals:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by animals")

'''If we want to create a new class for a specific type of animal, such as a dog, we can create a new class named "dog" that inherits from the animal class.'''
class Dog(animals):
    def __init__(self, name, breed):
        animals.__init__(self, name, species="dog")
        self.breed = breed
    
    def make_sound(self):
        print("bark!")

