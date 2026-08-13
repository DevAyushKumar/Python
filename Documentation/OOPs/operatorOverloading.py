'''operator overloading in Python: An introduction:
Operator overloading is a feature in Python that allows developers to redifine the behaviour of mathematical and comparison operator for custom datat types. This means that you can use the standard mathematical operators (+,-,*,/,etc.) and comparison operators (>,<,==,etc) in your own classes, just as you would for built-in data types like int, float and str.

Why do we need opeartor overloading ?
operator overloading allows you to create more reliable and intutive code. For instance, consider a custom class that represents a point in 2D space. You could define a meathod called 'add' to add two points together, but using the + operator makes the code more concise and redable.'''
p1 = Point(1,2)
p2 = point(3,4)
p3 = p1 + p2
print(p3.x, p3.x)