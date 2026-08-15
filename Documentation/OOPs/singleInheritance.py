'''Single Inheritance in Python:
Single inheritance is a type of inheritance when a class inherits properties and behaviours from a singlr parent class. This is the simplest and most common form of inheritance.

Synatx:
The synatx for single inheritance in Python is straightforward and easy to understand. To create a new class that inherits from a parent class, simply specify the parent class in the class defination, inside the parentheses, like this'''
'''class Childclass(parentClass):
    def __init__(self):
        pass'''

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

a = Dog("dog", "woof")
a.make_sound()
b = animals("dog", "german")
b.make_sound()

'''The dog class inherits all the attributes and behaviours of the animals class, including the __init__ meathod and the make_sound meathod. Additionally, the dog class has its own __init__ meathod that adds a new attribute for the breed of the dog, and it also overrides the make_sound meathod to sepcify the sound that a dog makes.

Single inheritance is a pwerful tool in Python that allows you to create new classes based on existing classes. It allows you to reuse the code, extend it to fit your needs, and make it easier to manage complex systems. understanding single inheritance is an immportant step in becoming proficient in object-oriented programming in python.'''
class cat(animals):
    def make_sound(self, breed):
        animals.__init__(self, name, species="cat")
        self.breed = breed

    def make_sound(self):
        print("meow")
    
    def cat_name(self):
        print("snowy")

c = cat("cat", "meow")
c.make_sound()
c.cat_name()