'''Opening file:
Before we can perform any operation on file, we must first open it. Python provides the open() function to open a file. It takes two arguments: the name of the file and the mode in which the file should be opened. The mode can be 'r' for reading. 'w' for writing or 'a' for appending.'''
f=open('myfile.txt', 'r')
'''By default, the open() function returns a file object that can be used to read from or write to the file, depending on the mode.

Mode in files:
There are various meathod to open a file:
1. read(r): this mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameters.
2. write(w): This mode opens the file for writing only and creates a new file if it does not exist.
3. append(a): This mode opens the file for appending only and creates a new file if the file does not exist. 
4. create(x): This mode creates a file and gives an error if the file already exists.
5. text(t): Apart from these modes we also need to specify how the file must be handled.t mode is used to handle text file. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the defualt. The default mode is 'r' (open for reading text, synonym of 'rt')'''

'''Reading from a file:
Once we have a file object, we can use various meathods to read from the file.
The read() meathod reads the entire contents of a file and returns a string
f=open("myfile.txt","r")
contents=f.read()
print(contents)

Writing to a file:
To write to a file, we first need to open it in the write mode
f=open("new.txt","w")
We can then use the write() meathod to write to the file
f=open("myfile.txt","w")
f.write("Hello world!")
Keep in mind that writing to a file will overwrite its content. If you want to append to a file insted of overwriting it, you can open it in append mode.
f=open("myfile.txt","a")
f.write("hello world!")'''

'''Closing a file: 
It is important to close a file after you are done with it. This releases resources used by the file and allows other programs to access it.
To close a file, you can use the close() meathod
f=open("myfile.txt,"r")
f.close()

The "with" statement:
Alternatively, you can use the with statement to automatically close the file after you are done with it.
with open("myfile.txt","r") as f:
    #do something
    f.close()'''