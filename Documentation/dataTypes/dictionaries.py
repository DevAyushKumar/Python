'''Python dictionaries:
Dictionaries are ordered collection of data items. They are store multiple items in a single variable. Dictionary items are key-value pairs that are seperated by commas and enclosed within curly brackets{}'''
info={"name":"karan", "age":19, "eligible":True}

#Accessing dictionary items
'''1. Accessing single values:
Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get meathod.'''
info={"name":"Ayush", "age":18,"eligible":True}
print(info["name"])

'''2. Accessing multiple values:
We can print all the values in the dictionary using values() meathod.'''
info={"nane":"Ayush", "age":18, "eligibility":True}
print(info.values())

'''3. Accessing keys:
We can print all the keys in the dictionary using keys() meathod.'''
info={"name":"Ayush","age":18,"eligibility":True}
print(info.keys())

'''4. Accessing key-value pairs:
We can print all the key-value pairs using the items() meathod.'''
info={"name":"Ayush","age":18,"eligibility":True}
print(info.items())
