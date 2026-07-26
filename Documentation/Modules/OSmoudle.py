'''OS module in python:
The OS module is a built-in library that provides functions for interacting with the operating system. It allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, and running system commands. 
Here are some common tasks you can perform with the os module:
Reading and writing files. The os module provides functions for opening, reading and writing files. For example, to open a file for reading, you can use the open function'''
import os
if (not os.path.exists("data")):
    os.mkdir("data")
for i in range(0,100):
    os.remove(f"data/Tutorial {i+1}")

'''Interacting with file system: 
The os module also provides functions for interacting with the file system. For example, you can use the os.lisdir function to get a list of the files in a directory. 
import os
files = os.listdir(".")
print(files)'''