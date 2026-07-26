'''Lambda function in python:
In python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword'''
#lambda arguments:expression
'''lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter and reduce.'''
def double(x):
    return x*2
lambda x:x*2
'''The above lambda function has the same functionallity as the double function defined earlier. However, the lambda function is anonymous, as it does not have a name.
Lambda functions can have multiple arguments, just like regular functions'''
lambda x,y:x+y
'''Lambda functions can have mulitple statements, but they are limited to a single expression:'''
lambda x,y:print(f"{x}+{y}={x+y}")
'''In the above example the lambda function includes a print statement, but it is limited to a single expression.
Lambda functions are often used to conjugate with higher-order functions, such as map,fiilter and reduce.'''