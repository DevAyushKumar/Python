'''Hybrid inheritance in Python:
Hybrid inheritance is a combination of multple inhertance and single inheritance in obejct-oriented programming. It is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into a single derived class, and a single inheritance is used to inherit the properties of derived class into a sub-derived class.

In Python, hybrid inheritance can be impplemented by creating a class hiearchy. In which a base class is inherited by multiple derived classes, and one of the derived classes is further inherited by a sub-derived class.

Syntax:
The syntax for implementing Hybrid Inheritance in Python in the same as for implementing Single inheritance, Multiple Inheritance or Hierarchical Inheritance.
'''

class human:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print(f"name {self.name}")
        print(f"age {self.age}")

class person(human):
    def __inti__(self, name, age, address):
        super().__init__(name, age)
        self.address = address

    def show_details(self):
        super().show_details()
        print(f"address: {self.address}")

class program:
    def __init__(self, program_name, duration):
        self.program_name = program_name
        self.duration = duration

    def show_program(self):
        print(f"program: {self.program_name} ({self.duration} years)")

class student(person):
    def __init__(self, name, age, address, program):
        super().__init__(name, age, address)
        self.program = program

    def show_details(self):
        super().show_details()
        self.program.show_program()

degree = program("computer science", 4)
student = student("john Dee", 22, "221B baker St", degree)
student.show_details()

'''Hierarchical Inheritance
Hierarchical Inheritance is a type of inheritance in Object-oriented programming where multiple subclass inherit from a single base class. In other words, a single base class acts as a parent class for multiple subclass. This is a way of establishing relationships between classes int a hierarchical manner.'''

class Animal:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print(f"Name: {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def show_details(self):
        super().show_details()
        print(f"Species: Dog | Breed: {self.breed}")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def show_details(self):
        super().show_details()
        print(f"Species: Cat | Color: {self.color}")

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Luna", "White")

dog.show_details()
cat.show_details()