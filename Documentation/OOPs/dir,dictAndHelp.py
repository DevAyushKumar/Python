#dir(), __dict__ and help() meathods in python
'''We must look into dir(), __dict__ and help() attribute/meathods in python. They make it easy for us to understand how classes resolve various functions and executes code. In python, there are there are built-in functions that are commonly used to get information about objects: dir(), dict and help(). Lets's take a look at each of them'''

'''The dir() meathod:
dir(): The dir() function returns a list of all the attributes and meathods (including dunder meathods) available for an object. It is a useful tool for discovering what you can do with an object'''
x = [1,2,3]
dir(x)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__','__getattribute__','__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__','__init__']

'''The __dict__ attribute:
__dict__: the __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection. Example:'''
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = person("Ayush", 18)
print(p.__dict__)

'''The help() meathod:
help(): The help() function is used to get help documentation for an object, including a description of its attributes and meathods.'''
help(str)

