'''Access modifiers and specifiers: 
Access modifiers and access specifiers in python programming are used to limit the access of class varibales and class meathods outside of class while implementing the conecpts of inheritance 

Types of access specifiers:
1. Public access modifiers
2. Private access modifiers 
3. Protected access modifiers'''

'''Public access specifers in Python:
All the variables and meathods (member function) in python are by default public. Any instance followed by a self keyword that is slef.var_name is public accessed. '''
class stu:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
obj = stu("Ayush", 150)
print(obj.name)
print(obj.rollno)

'''Private access modifiers:
By defination, private members of a class (variables or meathods) are those members which are only accessiable to those which are inside the class. We cannot use private members outside of class. 
In Python, there is no strict concept of "private" access modifiers like in some otehr programming languages. However, a convention has been established to indicate that a varibale meathod should be considered private by preffixing its name with a double underscore(__). This is known as "weak internal use indicator" and it is convention only, not a strict rule. Code outside the class can still access these "private" varibales in meathods, but it is genrally understood that they should not be accessed or modified. '''
class student:
    def __init__(self):
        self.__name = "Ayush"

a = student()
print(a._student__name)
'''Private mumbers of class cannot be accessed inheritance outside of class. If we try to access or to inherit the properties of private members to child class (derived class). The it will show the error.'''

'''Name Mangling:
Name mangling in Python is a techinque used to protect class-private and superclass-private attributes from being accidentaly overwritten by subclass. Names of class-private and superclass-private attributes are being transformed by the addition of a single leading underscore and a double leading underscore respctively. '''
class MyClass:
    def __init__(self):
        self._private_attribute = "I am private attribute"
        self.__mangled_attribute = "I am mangled attribute"
Obj1=MyClass()
print(Obj1._private_attribute)
print(Obj1._MyClass__mangled_attribute)