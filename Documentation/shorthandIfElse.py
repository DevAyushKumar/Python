#if...else in one line
'''There is also a shorthand syntax for the if-else statement that can be used when the condition being tested is simple and the code blocks to be executed are short. Here's an  example:'''
a=3
b=330
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a==b else print("B")

#Conclusion
'''The shorthand syntax can be a convienent way to write simple if-else statements, especially when you want to assign a value to a variable beased on a condition. However, its not suitable for more complex situations where you need to execute multiple statements or perform more complex logic. In those cases, it's best to use full if-else statement'''