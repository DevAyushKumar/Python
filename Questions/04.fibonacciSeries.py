num=int(input("Enter the number: "))
def series(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    sequence=[0,1]
    for i in range(2,num):
        next=sequence[-1]+sequence[-2]
        sequence.append(next)
    return sequence
print(series(num))