class library:

    def __init__(self):
        self.no_of_books = 0
        self.list_of_books = []

    def manage(self):
        a = int(input("Enter the number of books you want to enter: "))
        for i in range(a):
            book = input("Enter the name of the book: ")
            self.list_of_books.append(book)
            self.no_of_books += 1

    def show(self):
        if self.no_of_books == len(self.list_of_books):
            print(f"The number of books currently in the library is {self.no_of_books} \n")

        else:
            print("The number of books does not mathch the current books in library \n")

lib = library()
while(1):
    print("1. Enter the detail of book in library \n2. Show the details of books in library \n3. Exit \n")
    user = int(input("Enter your choice 1, 2 or 3: "))
    if user == 1:
        lib.manage()
    elif user == 2:
        lib.show()
    elif user == 3:
        exit()
    else:
        print("Invalid! Enter a valid choice")