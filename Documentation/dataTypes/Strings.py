'''What are strings in python ?
=> In python, anything that you enclose between single or double quotation marks is considered a string. A string is esssentially a sequence or array of textual data. Strings are used while working with unicode characters.
Note: It does not matter whether you enclose your strings in single or double quotes, the output remains the same.

Accessing characters in string:
In python, strings is like an array of characters. We can access parts of strings by using its index which starts from 0
ex: print(name[0])
print(name[1])

Looping through strings:
We can loop through strings by using 
for characters in name:
    print(characters)
Abvoe code prints characters in name one by one'''

name="Ayush"
print(name[0])
for characters in name:
    print(characters);