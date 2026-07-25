#seek() and tell() functions
'''In python, the seek() and tell() functions are used to work with the file objects and their positions within a file. These functions are part of the built-in modules, which provides a constant interface for reading and writing a various file-like objects, such as files, pipes and in-memory buffers.'''

'''seek() function:
The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward backward from the current position.'''
with open("file.txt","r") as f:
    f.seek(10)
    data=f.read(5)

'''tell() function:
the tell() function returns the current position within the file, in bytes. This can be useful for keeping track of your location within the file or for seeking to a specific positive relative to the current position.'''
with open("file.txt","r") as f:
    data=f.read(5)
    current_positon=f.tell()
    f.seek(current_positon)

'''truncate() function:
when you open a file in Python using the open function, you can specify the mode in which you want to open the file. If you specify the mode as  'w' or 'a', the file is opened in write mode and you can write in the file. However, if you want to truncate the file to a specific size, you can still truncate function.'''
with open("sample.txt","w")as f:
    f.write("Hello")
    f.truncate(5)

with open("sample.txt","r")as f:
    print(f.read())
    