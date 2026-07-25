'''How importing in python works:
Importing in python is the process of loading code from a Python module into the current script. This allows you to use the functions and varibales defined in the module in the current script, as well as any additional modules that are imported modules may depend on.
To import a module in Python, you use the import statement followed by the name of the module. For example, to import the math module, which contains the variety of mathematical functions, you would use the folloeing statement.
import math
Once the module is imported, you can use any of the functions and variables defined in the module using the dot notation. For example, to use the sqrt function from the math module, you would write'''

import math
a=9
result = math.sqrt(a)
print(result)

'''From keyword:
You can also use import specific functions or variables from the a module using the from keyword. For example, to import only the sqrt function from the math module, you would write'''

from math import sqrt
result = sqrt(9)
print(result)

'''You can also import multiple functions or varibales using the function at once'''
from math import sqrt,pi
result = sqrt(16)
print(result)
print(pi)

'''Importing everythin:
It's also possible to import all the functions and variables from a module using the * wildcard. However, this is generally not recommended as it can lead to confusion and make it harder to understand where specific functions and variables are coming from.'''
from math import *
result = sqrt(9)
print(pi)

'''Python also allows you to rename imported modules using the as keyword. This can be useful if you want to use a shorter or more descriptive name for a module, or if you want to avoid naming conflicts with other modules or variables in code.'''
import math as m
result=m.sqrt(9)
print(m.pi)

'''The dir function: 
Finally, Python has a built-in function called dir that you can use to view the names of all the functions and variables defined in a module. This can be helpful for exploring and understanding the contents of new module.'''
import math
print(dir(math))
'''This will output a list of all the names defined in the math module in the math module, including function like sqrt and pi, as well as other variables and constants.
In summary, the import statement in Python allows you to access the functions and variables defined in a module from within your current scripts. You can import the entire module, specific functions or variables, or use the * wildcard to import everything. You can also use the keyword to rename a module, and the dir function to view the contents of module.'''