'''Break statement:
The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within'''
for i in range(1,101,1):
    print(i, end="")
    if(i==50):
        break
    else:
        print('Mississipi')
print("Thank you")

'''Continue statement
The continue statement skips the rest of the loop statements and causes the next iteration to occur.'''
for i in [2,3,4,5,6,7,8]:
    if(i%2 !=0):
        continue
    print(i)