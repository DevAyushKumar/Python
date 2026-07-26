'''Getters:
Getters in python are meathods that are used to access the values of an object's properties. They are used to return the value of a specific property, and typically defined using the @property decorator. Here is an example of a simple with a getter meathod.'''
class MyClass:
    def __init__(self,value):
        self._value = value

    def show(self):
        print(f"The values is {self._value}")

    @property
    def value(self):
        return self._value
'''In this example, the MyClass class has a single property._value, which is initialized in the init meathod. The value meathod is defined as a getter using the @property decorator and is used to return the value of the _value property.
To use the getter, we can create an instance of the MyClass class, and then access the value property as if it were an attribute'''
obj = MyClass(10)
print(obj.value)
obj.show()

'''Setters:
It is important to note that the getters do not take any parameters and we cannot set the value through getter meathod. For that we need setter meathod which can be added by decorating meathod with @property_name.setter'''
class MyClass:
    def __init__(self,value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value