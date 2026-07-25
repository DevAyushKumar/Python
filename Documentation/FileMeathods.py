'''Readlines() meathods:
the readline() meathod reads a single line from the file. If you want to read multiple lines, we can use loop.'''
f=open("myfile.txt","r")
while True:
    line = f.readlines()
    if not line:
        break
    print(line)
'''The readlines() meathod reads all the lines of the file and returns them as a list of strings.'''

'''Writelines() meathod:
The writelines() meathod in Python writes a sequence of strings to a file. The sequence can be any iterable objects, such as list or tuple.'''
f=open("file.txt","w")
lines=["inex","dex","def"]
f.writelines(lines)
f.close()
'''This will wrtie the strings in the lines list to the file myfile.txt. The \n character are used to add newline characters to the end of the each string.
Keep in mind that the writelines() meathod does not add newline characters between strings in the sequence. If you want to add newlines between the strings, you can use a loop to write each strings seperately.'''
f=open("myfile.txt","r")
lines=["line 1 \n", "line 2 \n", "line 3 \n"]
for line in lines:
    f.write(line + "\n")
f.close()

