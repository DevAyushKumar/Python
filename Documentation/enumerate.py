'''Enumerate function in python:
To enumerate function in built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. Here's a basic example of how it works.'''
fruits=["Apple", "Banana", "mango"]
for index,fruit in enumerate(fruits):
    print(f"Index is {index} and fruits is {fruit}")
'''As you can see the enumerate function returns a tuple containing the index and value of each element in the sequence. You can use the for loop to unpack form tuples and assign them to a varibales, as shown in the above example'''

'''Changing the index: 
By default, the enumerate function starts the index at 0, but you can specify a different starting index by passing it as an argument to the enumerate function.'''
fruits=["Apple", "Banana","Mango"]
for index,fruit in enumerate(fruits, start=1):
    print(index, fruit)
'''The enumerate function is often used when you need to loop over a sequence and perform some action with both the index and value of each element. For example, you might use it to loop over a list of strings and print the index and value of each string in a formatted way:'''
fruits=["Apple", "Banana","Mango"]
for ind, fru in enumerate(fruits):
    print(f"{ind+1}: {fru}")

'''In addition to list, you can use the enumrate function with any other sequence type in python, such as tuple and strings. Here's an example with a tuple'''
colors=("red","green","Blue")
for index,color in enumerate(colors):
    print(f"{index}: {color}")

#Example with string
s="Hello"
for index,ch in enumerate(s):
    print(f"{index}: {ch}")