'''The time module in python:
The time module in Python provides a set of functions to work with the time-related operators, such as timekeeping, formetting, and time conversion. This module is part of the Python Standard Library and is available in all Python installations, making it a conveninent and essential tool for a wide range of applications. In this day 84 tutorial, we'll explore the time module in Python and see how it can be used in different sceneries.

time.time()
The time.time() function returns the current time as a floating-point number, representing the number of seconds since the speech (the point in time when the time module was initialized). The returned value is based on the computer's system clock and is affected by time adjustment made by the operating system, such as daylight saving time. Here's example '''

import time
print(time.time())

'''As you can see, the function returns the current time as a floating-point number, which can be used for various purposes, such as measuring the duration of an operator or the elapsed time since a certain point in time.

'''
def usingwhile():
    i=0
    while i<5000:
        i+=1
        print(i)

def usingfor():
    for i in range(5000):
        print(i)

init = time.time()


usingfor()
t1 = time.time() - init
usingwhile()
print(time.time() - init)
print(t1)

'''time.sleep():
The time.sleep() function suspends the execution of the current thread for a specified number of seconds. This function can be used to pause the program for a cretain period of time, allowing other parts of the program to run or to synchronize the execution of multiple threads.'''

print("start", time.time())
time.sleep(2)
print("end", time.time())