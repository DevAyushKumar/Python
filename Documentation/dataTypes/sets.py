'''Python sets:
Sets are unordered collection of data items. They store multiple items in a single variable. Set items are seperated by commas and enclosed with curly brackets {}. Sets are unchangable, meaning you cannot change items of the set once created. Sets do not contain duplicate items'''
info={"carlo",True, 19,False,5.9,19}
print(info)
'''here we see the items of sets occur in random order and hence they cannot be accessed using index numbers. Also do not allow duplicate values.'''
newset={}
print(type(newset))

'''Accessing set items:

Using for loop'''
info={"carlo",19,False,5.9}
for item in info:
    print(item)