#Class Meathods as alternative constructors
'''In Object-oriented programming, the term "constructor" refers to a special type of meathod that is automatically executed when an object is ceated from the class. The purpose of a constructor is to initialize the object's attributes, allowing the object to be fully functional and ready to use.

However, there are times when you may want to create an object in a different way, or with different initial values, then what is provided by the default construtor. This is where class meathods can be used as alternative constructors.

A class meathod belongs to the class rather than to an instance of class. One common use case for class meathods as alternative constructors is when you want to create an object from date that is stored in a different format, such as a string or a dictionary. For example, consider a class named "person" that has two attributes: "name" and "age". The default constructor for the class might look like this:'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

'''But what if you want to create a person object from a string that contains the person's name and age, seperated by a comma ? You can define a class meathod named "from_string" to do this'''
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))

'''Now you can create a person from a string like this:'''
per = person.from_string("Ayush, 18")
'''Another common use case for the class meathods as alternative constructors is when you want to create an object with a different set of default values then what is provided by the default constructor. For example, consider a class named "rectangle" that has two attributes: "width" and "height". The default constructor for the class might look like this'''
class Rectangles:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def square(cls, size):
        return cls(size, size)
'''Now you can create a square rectangle like this:'''
rectangle = Rectangles.square(10)