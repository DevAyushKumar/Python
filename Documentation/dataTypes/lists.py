'''Python Lists
* lists are ordered collection of data items.
* They store multiple items in a single words
* List items are seperated by commas and enclosed with square braackets []
* Lists are changable meaning we can after them after creation.'''
#Examples
list1 = [1,2,3,4,5,6,7,8]
list2 = ["Red", "green", "blue"]
print(list1)
print(list2)

'''List Indexing:
Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has the index [0], the second item has the index [1], the third item has the index [2]'''
list2=[1,2,3,4,5]
print(list2[2])

'''Accessing item list:
We can access list items by using its index with a square bracket[].

Positive indexing:
As we have seen that list items has positive index, as such we can access using these these indexes.

Negative indexing:
Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.'''
list3=["red", "green", "blue", "white"]
print(list3[-2])
print(list3[-3])

'''Check wether an item in present in the list?
We can also check whether the item is present in list or not'''
if "yellow" in list3:
    print("Yellow is present")
else:
    print('yellow is not present')

'''range of index:
You can print a range of list bby specifying where you want to start, where do you want to end and if you want to skip elements in between the range.'''
#syntax: listName=[start: end: jumpindex]

'''note: jump index is optional. we will see in later examples'''
animals=["cat","dog","cow","pig"]
print(animals[2:4])

'''Here we provide index of the element from where we want to start and end of index of the elements till which we want to print values.
Note: The element of the end indexe provided will not be included.

List comprehension:
List comprenhension are used for creating new lists from other iterable like lists, tuples, dictionaries, sets and even in arrays and strings.

Syntax:
List = [expression(item) for item in iterable if condition]
Exression: It is the item which is being iterated.
Iterable: It can be list, tuples, dictionaries, sets and even in arrays and strings.
Condition: Condition checks if the item should be added to the new list or not.'''
#example
name = ["Milo", "sarah", "Ayush", "adam"]
namesWith_o = [item for item in name if "o" in item]
print(namesWith_o)