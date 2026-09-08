questions="What is the name of current pm"
options="A.Narendra Modi | B.option 2 | C. option 3 | D.option 4"
numberOfQuestions=1
opt=options.split("|")
points=0
le=len(opt)
for i in range(le):
    option=opt[0].strip()
for i in range(numberOfQuestions):
    print(questions)
    print(options)
    Op1=input("Enter the Option: ")
    for i in range(le):
        if(option[i][0].upper==Op1.upper):
            points +=1
        else:
            continue


print("Your points is: ", points)