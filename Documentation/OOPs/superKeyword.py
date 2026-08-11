'''Super keyword in python: 
The upper() keyword in Python is used to refer to the present class. It is especially useful when a class inherits from multiple parent classes and you want to call a meathod from one of the parent classes.

When a class inherits from a parent class, it can override or extend the meathods defined to the parent class. However, sometimes you might want to use the parent class meathod in the child class. This is where the super() keyword comes in handy.

here's an example of how to use the super() keyword in a single inheritance scennario.'''
class ParentClass:
    def parent_meathod(self):
        print("This is the parent meathod. ")

class ChildClass(ParentClass):
    def Child_meathod(self):
        print("This is the child meathod.")
        super().parent_meathod()

child_object = ChildClass()
child_object.Child_meathod()


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

Rishu = Employee("Rishu", "120")
Ayush = Programmer("Ayush", "150", "Python")
print(Ayush.name)
print(Ayush.id)
print(Ayush.lang)