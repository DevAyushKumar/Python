'''Multilevel Inheritance in Python
Multilevel inheritance is a type of inheritance in object-oriented programming where a derived class inherits from another class. This type of inheritance allows you to build a hierarchy of classes where one class builds upon another, leading to a ore specialized class.

In Python, multilevel inheritance is achieved using the class hierarchy. The syntax for multilevel inheritance is quite simple and follows the same syntax as a single inheritance

syntax:
class BaseClass:
    #base class code

class DerivedClass1:
    #Derived class 1 code
    
class DerivedClass2:
    #Derived class 2 code

In the above example, we have three classes: BaseClass, DerivedClass1 and DerivedClass2. The derived class inherits from the BaseClass and the DerivedClass2 inheris from the DerivedClass1 class. This creates a hierarchy where DerivedClass2 has access to all the attributes and meathods of both DerivedClass1 and BaseClass

Example:'''
class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"species: {self.species}")

class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name, species="dog")
        self.breed = breed

class GoldenRetriver(dog):
    def __init__(self, name, colour):
        dog.__init__(self, name, breed="golden retriver")
        self.colour = colour

    def show_details(self):
        dog.show_details(self)
        print(f"colour {self.colour}")

o = GoldenRetriver("bob", "brown")
o.show_details()

'''As we can see from the output, the GoldenRetriver object has access to all the attributes and meathods of the Animal and Dog classes, and, it has also added its own unique attributes and meathods. This is a powerful feature of multilevel inheritance, as it allows you to create more complex and indicate classes by building upon existing ones.

Another important aspect of multilevl inheritance is that it allows you to reuse the code and avoid repeating the same logic multiple times. This can lead to better maintaibility and readability of your code, as you can abstract away complex logic into base classes and build upon them.

In conclusion, multilevel inheritance is a powerful feature in object-oriented programming that allows you to create complete and indicate classes by building upon existing ones. It provides the benefits of code reuse, maintainability and readibility while also requiring careful consideration to avoid potentional problems.'''