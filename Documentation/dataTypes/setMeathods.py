'''Joining sets:
Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the sets just like in mathematics.

1. Union() and Update():
The union() and update() meathods prints all items that are present in the two sets. The union() meathod returns a new set whereas update() meathod adds item into the existing set from another set.'''
cities={"Madrid","spain","portugal"}
cities2={"India","Pakistan","China"}
cities3=cities.union(cities2)
print(cities3)

'''Intersection() and intersection_update():
The intersection() and intersection_update() meathod prints only items that are similar to both the sets. The intersection() meathod returns a new set whereas intersection_update() meathod updates into the existing set from another set.'''
cities={"Madrid","spain","portugal"}
cities2={"India","Pakistan","China"}
cities3=cities.intersection_update(cities2)
print(cities)

'''Symmetric_difference and symmetric_difference_update():
The symmetric_difference() and symmteric_difference_update() meathod prints only items that are not similar to both the sets. The symmetric_difference() meathod returns a new set whereas symmeteric_difference_update() meathod updates the existing set from another set.'''
cities={"Madrid","spain","portugal"}
cities2={"India","Pakistan","China"}
cities.symmetric_difference_update(cities2)
print(cities)

'''Difference() and difference_update():
The difference() difference_update() meathods prints only items that are only present in the original set and not in both the sets. The difference() and difference_update() meathods returns a new set whereas difference_update() meathod updates into the existing set form another set.'''
cities={"Madrid","spain","portugal"}
cities2={"India","Pakistan","China"}
cities3=cities.difference_update(cities2)
print(cities3)

'''Set meathods:
There are several in-built meathods used for the manipulation of set. They are explained below.

isdisjoint():
The isdisjoint() meathod checks if items of given set are present in another set. This meathod returns False if items are present, else it returns True.'''
cities={"Madrid","spain","portugal"}
cities2={"India","Pakistan","China"}
print(cities.isdisjoint(cities2))

'''issuperset():
The issuperset() meathod checks if all the items of a particular set are present in original set. It returns True if all the items are present, else it returns False'''
cities={"Madrid","spain","portugal"}
cities2={"India","Pakistan","China"}
print(cities.issuperset(cities2))

'''issubset():
the issubset() meathod checks if all the items of the original set are present in the particular set. It returns true if all the elemets are present, else it returns false'''
cities={"Madrid","spain","portugal"}
cities2={"India","Pakistan","China"}
print(cities2.issubset(cities))

'''add():
If you want to add a single item in a set then use add() meathod'''
cities={"Madrid","spain","portugal"}
cities.add("India")
print(cities)

'''remove():
If you want to add more than one item, simply create another set or any other iterable object(list,tuple,dictionary) and use the update() meathod to add it into the existing set.'''
cities={"Madrid","spain","portugal"}
cities2={"India","Pakistan","China"}
cities.update(cities2)
print(cities)

'''Remove()/discard():
We can use remove() and discard() meathods to remove items from the list.'''
cities={"Madrid","spain","portugal"}
cities.remove("spain")
print(cities)
'''The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error'''

'''pop():
This meathod removes the last item of the set but the catch is that if we don't know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() meathod to a variable.'''
cities={"Madrid","spain","portugal"}
item=cities.pop()
print(cities)
print(item)

'''del:
del is not a meathod, rather it is a keyword which deletes the set entirely'''

'''clear():
This meathod clears all items in the set and prints an empty set.'''
cities={"Madrid","spain","portugal"}
cities.clear()
print(cities)

'''check if an item exists:
you can also check if the items is present in the set or not.'''
info={"carlo",19,False,5.9}
if "carlo" in info:
    print("carlo is present")
else:
    print("carlo is not present")