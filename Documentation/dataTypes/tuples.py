'''Python Tuples:
Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are seperated by commas and enclosed with round brackets (). Tuples are unchangable meaning we can not alter them after creation.'''
tuple1=(1,2,3,4,5,6)
tuple2=("Red","green","blue")
print(tuple1)
print(tuple2)

'''Tuple indexes:
Each item/element in a tuple has its own unique index. This index can be used to
access any particular item from the tuple. The first item has index [0], second item has index[1], third item has index[2] and so on'''
country=["Spain","italy","india"]

'''Accessing Tuple items:
1. Positive indexing:
As we have seen that tuple item has index, as such we can access items using these indexes.'''
country=["spain","italy","india"]
print(country[0])

'''Check for item:
We can check if a given item is present in the tuple. This is done using the in keyword'''
country=["Spain","india","germany"]
if "germany" in country:
    print("Germany is present")
else:
    print("germany is not present")

'''Range of index:
You can print a range of tuple item by specifying where do you want to start, where do you want to end and if you want to skip elements in between the range.
syntax: [start:end:jumpindex]
Note: jump index is optional. We will see this again in the examples'''
animals=["cat","dog","cow","pig"]
print(animals[1:])