'''Access modifiers and specifiers: 
Access modifiers and access specifiers in python programming are used to limit the access of class varibales and class meathods outside of class while implementing the conecpts of inheritance 

Types of access specifiers:
1. Public access modifiers
2. Private access modifiers 
3. Protected access modifiers'''

'''Public access specifers in Python:
All the variables and meathods (member function) in python are by default public. Any instance followed by a self keyword that is slef.var_name is public accessed. '''
class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
obj = student("Ayush", 150)
print(obj.name)
print(obj.rollno)
