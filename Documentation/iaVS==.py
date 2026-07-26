#is VS == in Python
'''In Python, is and == are both comparison operators that can be used to check if two values are equal. However, there are some important differences between the two that you should be aware of.

the is operator compares the identity of two objects, while the == operator compares the values of the objects. This means that it will only return True if the objects being compared are the exact same objects in the memory, while == will return True if the object have the same value.'''

a=[1,2,3,4]
b=[1,2,3,4]
print(a==b)
print(a is b)
'''In this case, a and b are two seperate lists that have the same values, so == returns True. However, a and b are not the same object in memory, so it returns False.

One important thing to note is that, in Python, strings and integers are immutable, which means that once they are created, their value cannot be changed. This means that, for strings and integers, is and == will always return the same result.'''
a="hello"
b="hello"
c=4
d=5
print(a==b,c==d)
print(a is b,c==d)
'''In these cases, a and b are both pointing to the same object in memory, so is and == both return True.

For mutable objects such as lists and dictionaries, is and == can behave differently. In general, you should use == when you want to compare the values of two objects, and use is when you want to check if two objects are the same in memory.'''