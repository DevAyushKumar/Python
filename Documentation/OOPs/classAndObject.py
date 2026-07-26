#Pyhton classes and objects
'''A class is a blueprint or a template for creating objects, providing initial valuesfor state (member variable or attributes) and implemetations of behaviour (member functions or meathods).The user-defined objects are created using the class keyword.'''

'''Creating a class:'''
class details:
    name="Ayush"
    age=18
    def info(self):
        print(f"{self.name} has age {self.age}")

'''Creating an object:
Object is an inheritance of the class used to access the properties of the class now lets create an object of the class'''

obj1 = details()
print(obj1.name)
print(obj1.age)

'''Self parameter:
The self parameter is a referance to the current instances of the class, and is used to access variables that belong to the class.
It must be provided as the extra parameter inside the meathod definations.'''
class students:
    name = "Ayush"
    age = 18

    def des(self):
        print("my name is",self.name,"and i am",self.age,"years old")

obj2=students()
obj2.des()
