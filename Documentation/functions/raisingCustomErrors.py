#Raising custom errors
'''In python, we can raise custom errors by using the raise keyword.'''
salary=int(input('Enter your salary: '))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")
'''In previous tutorials, we learnt about the different built-in exceptions in python and why it is important to handle exceptions. However, sometimes we may need to create our own custom exceptions that serve our purpose'''

#Defining custom exceptions
'''In python, we can define our custom exceptions by creating a new class that is derived from the built-in exception case'''
class CustomError(Exception):
    #code
    pass
try:
    #code 
    pass
except:
    #customError
    pass
'''This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending an error report to the admin, calling an api, etc. '''