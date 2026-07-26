'''LOOPS IN PYTHON:
Sometimes a programmer wants to execute a group of statements a cetrain number of times. This can be done using loops. Based on this loops are further classified into following types: for loop, while loop, nested loop

For loop:
for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but itering over strings, lists, tuples, set and dictionaries'''
#example:
name = "Ayush"
for characters in name:
    print(characters, end='')
print('\n')
'''Rage():
What if we do not want to iterate over a sequence ?
what if we want to use for loop for a specific number of times ?'''
#example:
for i in range(5):
    print(i,end='')
print('\n')