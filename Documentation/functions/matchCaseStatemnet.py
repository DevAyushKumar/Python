'''MATCH CASE STATEMENT:
To implement switch case like characteristics very similar to if-else functionality, we use match case in pythonv
A match case statement will compare a given variable's value to different shapes, also reffered to as the pattern. The main idea is to keep on comparing the variable with the present pattern until it fits into one.

The switch case consists of three main entities:
1. The match keyword 
2. One or more case clauses
3. Expression for each case

The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches'''

#Example:
x=4
match x:
    case _ if x%2 != 0:
        print('x is 0')
    case _ if x%2 == 0: 
        print("x is 4")
    case _:
        print('x is a number')