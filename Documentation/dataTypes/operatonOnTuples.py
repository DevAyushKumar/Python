'''Manipulating tuples:
Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert a tuple to a list. Then perform operation on that list and convert it back to tuple'''
countries=["spain","italy","england","india","germany"]
temp=list(countries)
temp.append("Russia")
temp.pop(3)
temp[2]="Finland"
countries=tuple(temp)
print(countries)
'''Thus, we convert tuple to a list, manipulate items of the list using list meathods, then convert list back to a tuple.

However, we can directly concatenate two tuples without converting them to list'''
countries=("spain","italy","japan","india")
countries1=("Pakistan","Bangladesh")
asia = (countries+countries1)
print(asia)

'''Count():
The count() meathod of tuple returns the number of lines of the given element appears in the tuple.'''
#syntax: tuple.count(element)

tuple1=(1,2,3,4,5,2,7,8,9,2)
res = tuple1.count(2)
print(res)

'''index():
The index() meathood returns the first occurance of the given element from the tuple
Syntax: tuple.index(element, start, end)
Note: This meathod raises a Value Error if the element is not found in the tuple.'''
tuple1=(1,2,3,4,5,5,4,3,2,1)
res = tuple1.index(2)
