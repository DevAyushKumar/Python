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

'''Protected access modifiers:
In Object - Oreinted programming (OOP), the term protected is used to describe a member (i.e a meathod or attribute)of a class that is intended to be accessed only by the class itself and its subclass. In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_). For example, if a class has a meathod called _my_meathod, it is indicating that the meathod should only be accessed by the class itseld and its subclass. 
It's important to note that the single underscore is just a naming convention, and does not actually provide aby protection or restrict access to the member. The syntax we follow to make any varibale protected is to write variable name followed by a single underscore(_) ie._varname'''

class Name:
    def __init__(self):
        self._name = "Ayush"

    def _func(self):
        return "code with harry"

class subject(Name):
    pass

obj4 = Name()
obj5 = subject()

#calling by object of student class
print(obj4._name)
print(obj4._func())

#calling by object of subject class
print(obj5._name)
print(obj5._func())