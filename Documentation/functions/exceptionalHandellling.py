'''Exceptional handeling:
Exception handeling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handelling deals with these events to avoid the program or system crashing, without this process, exceptions would disrupt the normal operation of program.'''

#Exceptions in python
'''Python has many built-in exceptions that are raised when your program encounters an error(something wrong in program)
With these exceptions occur, the python interpreter stops the current process and passes it to the calling process until it is handeled. If not handeled, then program will crash.'''

#python try except
'''try..excpet blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executeed'''
try:
    for i in range(1,11):
        a=i+i
        print(a)
except:
    print("Invalid output")