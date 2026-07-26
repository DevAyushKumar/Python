''' STRING SLICING AND OPERATIONS ON STRING
Length of string:
We can find length of string using len() function'''
name = "Ayush"
print(len(name))
b=name[0:-3]
print(len(b))

'''String as an array:
A string is essentially a sequence of characters also called an array. Thus we can access the elements of an array.'''
fruit = "mango"
print(fruit[0:2])
print(fruit[3:-1])

'''Loop throguh an string:
Strings as an array are iterable. Thus we can loop throgh strings'''
alphabet = "MyWorld"
for word in alphabet:
    print(word)