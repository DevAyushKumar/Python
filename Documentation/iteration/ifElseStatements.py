'''IF-ELSE STATEMENT:
Sometimes the programmer needs to check the evalutation of certain expression(s), whether the expression(s) evalute true or false, then the program execution follows a different path then it would have if the expression had evalutaed true
Types of if-else statemets:
=> if
=> if-else
=> if-else-elif
=> nested if-else-elif
'''
#example:
price=180
budget=100
if price>=budget:
    print("Add the item to the cart")
else:
    print("Leave it, its out of budget")

#Example of if-else-elif
num=0
if (num<0):
    print("Number is greater than 0")
elif (num==0):
    print("Number is 0")
else:
    print("Number is less than 0")

#Example of if-else-elif
num1=10
if(num1>0):
    if(num1>0 and num1<=10):
        print("Number is between 1 to 10")
    elif(num1>10 and num1<=50):
        print("Number is between 11 to 50")
    else:
        print("Number is bigger than 50")
elif(num1==0):
    print("Number is 0")
else:
    print("Number is negative number")

