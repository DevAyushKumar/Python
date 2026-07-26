'''String meathods:
Python provides a set of built-in meathods to alter and modify strings.
1. Upper():
The upper() meathod converts a string to upper case'''
str1="This is a string"
print(str1.upper())

'''2. Lower():
The lower() meathod converts a string to lower case'''
str2="THIS IS A STRING"
print(str2.lower())

'''3. Strip():
The strip() meathod removes any spaces before and after the string'''
str3="  This is a string  "
print(str3.strip())

'''4. rstrip():
The rstrip() meathod removes all the trailing characters'''
str4="This is a string!!!"
print(str4.rstrip("!"))

'''5. replace():
The replace() meathod replaces all occurace of a string with another string'''
str5="This is a string"
print(str5.replace("is","was"))

'''6. split():
This split() meathod splits the given string at the specific instances and return the seperated string as a list items'''
str6="This is a string"
print(str6.split())

'''7. capitalize():
This capitalize() meathod turns only the first character of the string to uppercase and the rest other characters of the string are turned to the lowercase. The string has no effect if the first character is already uppercase.'''
str7="this is a string"
print(str7.capitalize())

'''8. Centre():
This centre() meathod aligns the string to the centre as per the parameters given by the user
We can also provide padding characters. It will fill the rest of characters provided by the user.'''
str8="This is the center code"
print(str8.center(50))

'''9. Count():
The count() meathod returns the number of lines the given value has occured within the given string'''
str9="this is a string"
print(str8.count("a"))

'''10. Endswith():
The endswith() meathod checks if the string ends with a given value. If yes then return true else return false.
We can also check the value in between the string by providing start and end index function'''
str10="This is a string"
print(str10.endswith("string"))

'''11.Find():
The find() meathod searches for the list occurance of the given value and returns the index where it is present. If given value is absent from the string then return -1.'''
str11="This is a string"
print(str11.find("a"))

'''12. isalnum():
The isalnum() meathod returns True only if the entire string only consists of a-z, A-Z, 0-9. If any other characters of puncutations is present then it returns false.'''
str12="This is a string"
print(str11.isalnum())

'''13. isalpha():
The isalpha() meathod returns True only if the entire string only consists of A-Z, a-z. If any other characters or puncutations or numbers(0-9) are present, then it returns false'''
str13="This is a string"
print(str13.isalpha())

'''14. islower():
The islower() meathod returns True only if all the characters in the string are lower case, else it returns false'''
str14="This is a string"
print(str14.islower())

'''15. isprintable():
The isprintable() meathod returns true only if all the values in the given string is printable, if not, then it returns false'''
str15="This is string"
print(str15.isprintable())

'''16. isspace():
The isspace() meathod returns true only and only if the string contains white spaces else it returns false'''
str16="This is a string"
print(str16.isspace())

'''17. istitle():
The istitle() meathod returns True only if the first letter of each word of the string is capatilazed, else it returns false.'''
str17="This is a string"
print(str17.istitle())

'''18. isupper():
The isupper() meathod returns True only if all the characters in the string are upper case, else it returns false'''
str18="This is a string"
print(str18.isupper())

'''19. swapcase():
The swapcase() meathod changes the character casing of the string. upper case are converted to lower case and lower case to upper case'''
str19="This is a string"
print(str19.swapcase())

'''20. title():
The title() meathod capatilizes each letter of the word within the string'''
str20="This is a string"
print(str20.title())