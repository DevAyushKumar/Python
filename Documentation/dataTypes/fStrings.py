'''String formatting in python
String formatting can be done in python using the fomat meathod'''
txt="For only {price:.2f} dollars!"
print(txt.format(price=49))

'''f-string in python:
It is a new string formatting mechanish introduced by the PEP 498. It is also known as Literal string Interpolation or more commonly as F-string (if characters preceding with the string literal). The primary focus of this mechanism is to make the interpolation easier.
When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be formatted in much same as the str.format() meathod. The f-string offers a convinent way to embed Python expression inside string literal for formatting.'''
val="Geeks"
print(f"{val} for {val} is a portal for {val}")
'''In the above code, we have used the f-string to format the string. It evaluates at runtime: we can put all the valid Python expression in them'''
print(f"{2*30}")