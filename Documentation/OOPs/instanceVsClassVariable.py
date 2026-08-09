'''Instance vs class variables:
In python, variables can be defined at the class level or at the instance level. Understanding the difference between these types of variables is crucial for writing efficient and maintaining code.

Class Varibales:
Class variables are defined at the class level and are shared amoung all instances of the class. They are defined outside of any meathod and are usally used to store information that is common to all instances of the class. For example, a class variable can be used to store the number of instances of a class that have been created.'''
class MyClass:
    class_variable = 0

    def __init__(self):
        MyClass.class_variable+=1

    def cl_var(self):
        print(MyClass.class_variable)

obj1=MyClass()
obj2=MyClass()

obj1.cl_var()