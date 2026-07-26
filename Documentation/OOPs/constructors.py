'''Constructors:
A constructor is a special meathod in a class used to create and initialize an object of a class. There are different types of constructors. Constructors are invoked automatically when an object of a class is created.
A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other that none.'''
#syntax of constructor
def __init__(self):
    #initializations
    a=10
'''init is one the reserved functions in Python. In Object Oriented Programming, it is known as constructor. We can also create constructor by defining the function name with same class name'''
#syntax
class ABC:
    def ABC(self):
        #initialization
        a=10

'''Types of constructors in Python:
1. Parameterized constructor
2. Default constructor'''

'''Parameterized constructor:
When the constructor accepts the arguments along with self, it is known as parameterized constructor.
These arguments can be used inside the class the assign the values of the data members.'''
#syntax
class details:
    def __init__(self, animal, group):
        self.animal=animal
        self.group=group

obj3 = details("crab","seacreatures")
print(obj3.animal,"belong to",obj3.group)

'''Default constructor in Python:
When the constructor dosen't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.'''
class Details:

    def __inti__(self):
        print("crab belongs to the sea animals")

obj4=Details()