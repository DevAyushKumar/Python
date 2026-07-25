'''Local and global variables in python: 
A local variable is a variable that is defined within a function and is only accessible within the function. It is created when the function is called and destroyed when the function returns. 
On the other hand, a global variable is a variable that is defined outside of a function and is accessiable from within any functions in your code. '''
x=10 #global
def funk():
    y=20 #local
    print(x)
    print(y)
print(x)
funk()

'''The global keyword: 
What if we want to modify a global variable from within a function ? this is where the global veriables and should be accessed from the global scope.'''
a=1
def funk():
    global a
    a=2
    print(a)
print(a)
funk()

'''In this example, we used the global keyword to declare that we want to modify the global varibale x from within the function. As a result, the value of x is changed to 5.

It's important to note that it's generally considered good practice to avoid modifying global variables from within functions, as it can lead to unexpcted behaviour and make your code code harder to debug.'''