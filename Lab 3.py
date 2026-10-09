myBookList = []
myAuthorList = []
myUserList = []

class Book:

    def __init__(self):
        self.book_id = ""
        self.book_title = ""
        self.author_id = ""
        self.publisher = ""
        self.year_of_publication = ""

    def add_book(self):
        self.book_id = input("Enter book id: ")
        self.book_title = input("Enter book title: ")
        self.author_id = input("Enter author id: ")
        self.publisher = input("Enter publisher: ")
        self.year_of_publication = input("Enter year of publication: ")

    def print_info(self):
        print("Book ID:", self.book_id)
        print("Book Title:", self.book_title)
        print("Author ID:", self.author_id)
        print("Publisher:", self.publisher)
        print("Year of publication:", self.year_of_publication)

class Author:
    def __init__(self):
        self.author_id = ""
        self.author_name = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.email = ""

    def add_author(self):
        self.author_id = input("Enter author id: ")
        self.author_name = input("Enter author name: ")
        self.affiliation = input("Enter affiliation: ")
        self.country = input("Enter Country: ")
        self.phone = input("Enter phone number: ")
        self.email = input("Enter email: ")

    def print_info(self):
        print("Author:", self.author_id)
        print("Author Name:", self.author_name)
        print("Affiliation:", self.affiliation)
        print("Author Country:", self.country)
        print("Phone:", self.phone)
        print("Email:", self.email)

class User:
    def __init__(self):
        self.user_id = ""
        self.user_name = ""
        self.password = ""
        self.address = ""
        self.phone = ""
        self.email = ""
        self.books_borrowed = []

    def add_user(self):
        self.user_id = input("Enter user id: ")
        self.user_name = input("Enter user name: ")
        self.password = input("Enter password: ")
        self.address = input("Enter address: ")
        self.phone = input("Enter phone number: ")
        self.email = input("Enter email: ")

    def borrow_book(self, book_id):
        self.books_borrowed.append(book_id)

    def print_info(self):
        print("User ID:", self.user_id)
        print("User Name:", self.user_name)
        print("Password:", self.password)
        print("Address:", self.address)
        print("Phone:", self.phone)
        print("Email:", self.email)
        print("Books Borrowed:", self.books_borrowed)

while True:
    print("Library Management System")
    print("Menu:")
    print("1. Add Author")
    print("2. Add Book")
    print("3. Add User")
    print("4. Borrow Book")
    print("5. Display All Info")
    print("6. Exit")

    choice = int(input("Enter your choice: "))


    if choice == 1:
        aut = Author()
        aut.add_author()
        myAuthorList.append(aut)
        print("Author Added successfully.")


    elif choice == 2:
        book = Book()
        book.add_book()
        myBookList.append(book)
        print("Book Added successfully.")


    elif choice == 3:
        user = User()
        user.add_user()
        myUserList.append(user)
        print("User Added successfully.")

    elif choice == 4:
        user_id = input("Enter user id: ")
        book_id = input("Enter book id to borrow: ")

        for user in myUserList:
            if user.user_id == user_id:
                user.borrow_book(book_id)

        print("Book borrowed successfully.")


    elif choice == 5:
        print("AUTHORS")
        for aut in myAuthorList:
            aut.print_info()
            print("---------------")
        print("BOOKS")
        for book in myBookList:
            book.print_info()
            print("---------------")
        print("USERS")
        for user in myUserList:
            user.print_info()
            print("---------------")

    elif choice == 6:
        print("Exiting Program...")
        break

    else:
        print("Invalid choice.")


