# LIST MEATHODS

'''List.sort():
This meathod sorts the list in ascending order. The original list is updated.'''
colours=["Red", "Blue", "Green"]
colours.sort()
print(colours)
'''What if you want to print the list in descending order ?
We must give reverse=True as a parameter in the sort meathod.
The reverse parameter is set to False by default.
Note: Do not mistake the reverse parameters with the reversed meathod.

Reverse():
This meathod reverses the order of the list.'''
colours=["violet", "Red", "Blue", "green"]
colours.reverse()
print(colours)

'''Index():
This meathod returns the index of the first ocuurance of the list item.'''
num=[1,2,3,4,5,8,3]
print(num.index(3))

'''Count():
Returns the count of the number of items with the given value'''
num1=[1,2,3,4,5,6,7,3]
print(num1.count(3))

'''Copy():
Returns copy of the list. This can be done to perform operations on the list without modifying the original list.'''
num2=[1,2,3,4,5,5,4,3,2,1]
newls=num2.copy()
print(newls)

'''Appends():
This meathod appends items to the end of the existing list'''
color=["red","blue","green","yellow"]
color.append("violet")
print(color)

'''Insert():
This meathod inserts an item at the given index. User has to specify index and the item to be inserted within the insert() meathod'''
colours=["Violet", "red", "Green", "Yellow"]
colours.insert(1,"blue")
print(colours)

'''Extend():
This meathod adds an entire list or any other collection datatype(set,tuple,dictionary) to an exising list.'''
colours=["Violet", "indigo", "red"]
rainbow=["Blue", "green", "Yellow"]
colours.extend(rainbow)
print(colours)

'''Concatening two list:
You can simple concate two lists to join two lists'''
colours=["Violet","red","Green","Blue"]
colours2=["Brown","Yellow"]
print(colours+colours2)

