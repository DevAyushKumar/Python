stack = []
while(1):
    print("1.Push \n2.Pop \n3.Show \n4.Exit")
    a=int(input("Enter your choice: "))

    if(a==1):
        num = int(input("Enter the number: "))
        stack.append(num)
    elif(a==2):
        stack.pop()
    elif(a==3):
        print(stack)
    elif(a==4):
        exit()
    else:
        print("please enter a valid option")