'''Dictionaries meathods:
Dictionaries uses several built-in meathods for manipulation. They are listed below.

update(): 
The update() meathod updates the value of the key provided to it if the item already exists in the dictionary, else it contains a new key-value pair.'''
info={"name":"Ayush","age":18,"eligibility":True}
print(info)
info.update({"age":19})
info.update({"DOB":22})
print(info)

'''Removing item from dictionary:
There are a few meathods that we can use to remove items from the dictionary.

clear():
The clear() meathod removes all the items from the list.'''
info={"name":"Ayush","age":18,"eligibility":True}
info.clear()
print(info)

'''pop():
The pop() meathod removes the key-value pair whose key-value pair whose key is passed as a parameter.'''
info={"name":"Ayush","age":18,"eligible":True}
info.pop("eligible")
print(info)

'''popitem():
The popitem() meathod removes the last key-value pair from the dictionary.'''
info={"name":"Ayush","age":18,"eligibility":True}
info.popitem()
print(info)

'''del:
We can also use the del keyword to remove a dictionary item.'''
info={"name":"Ayush","age":18,"eligibility":True}
del info["eligibility"]
print(info)
'''If key is not provided, then the del keyword will delete the dictionary entirely'''

#Dictionary meathods
'''Dictionary uses several built-in meathods for manipulation. They are listed below.

Update(): 
the update() meathod updates the value of the key provided to it as if the item already exists in the dictionary, else it create a new key-value pair.'''
info={"name":"Ayush","age":18,"eligibility":True}
print(info)
info.update({"age":19})
info.update({"DOB":22})
print(info)

'''Removing items from dictionary:
There are few meathods that we can use to remove from dictionary.'''