#Finally clause
'''The finally code is also a part of exception handeling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding task like closing file resources or closing databse connection or may be ending the program execution with a delightful message.'''
try:
    #checks the code
    print("Code is right")
except:
    print("Code has errors")
    #Activates if code has exception
finally:
    print("Always executed")
    #always executed
'''The finally block is executed irrespective of the outcome of try...expect...else blocks.
One of the important use cases of finally block is the function which returns a value'''