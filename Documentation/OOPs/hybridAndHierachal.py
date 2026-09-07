'''Hybrid inheritance in Python:
Hybrid inheritance is a combination of multple inhertance and single inheritance in obejct-oriented programming. It is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into a single derived class, and a single inheritance is used to inherit the properties of derived class into a sub-derived class.

In Python, hybrid inheritance can be impplemented by creating a class hiearchy. In which a base class is inherited by multiple derived classes, and one of the derived classes is further inherited by a sub-derived class.

Syntax:
The syntax for implementing Hybrid Inheritance in Python in the same as for implementing Single inheritance, Multiple Inheritance or Hierarchical Inheritance.
'''
class BaseClass:
    pass

class DerivedClass1(BaseClass):
    pass

class DerivedClass2(DerivedClass1):
    pass

class DerivedClass3(DerivedClass1, DerivedClass2):
    pass

