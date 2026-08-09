'''Instance vs class variables:
In python, variables can be defined at the class level or at the instance level. Understanding the difference between these types of variables is crucial for writing efficient and maintaining code.

Class Varibales:
Class variables are defined at the class level and are shared amoung all instances of the class. They are defined outside of any meathod and are usally used to store information that is common to all instances of the class. For example, a class variable can be used to store the number of instances of a class that have been created.'''
class employe:
    def __init__(self, name):
        self.name = name
        self.raise_ammount = 0.02
    
    def intro(self):
        print(f"The name of employee is {self.name} and raise is {self.raise_ammount}")

emp1 = employe("Ayush")
emp1.raise_ammount = 0.3
employe.intro(emp1)
emp2 = employe("Rishu")
employe.intro(emp2)
'''In this example, the shared class vaiable is shared among all instances of the clas MyClass. When we create a new instances of MyClass, the value of class_variable is incremented. When we call the print_class_variable meathod on obj1 and obj2, we get the same value of class_variable.

Instance Variables:
Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init meathod and are usually used to store information that is specific to each instance of the class. For example, an instance variable can be used to store the name of an employee in a class that represents an employee.'''

class MyClass:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

obj3 = MyClass("Ayush")
obj3.print_name()