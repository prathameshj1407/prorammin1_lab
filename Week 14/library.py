
class LibraryManagement:
    def __init__(self):
        self.booklist = []
        self.borrowlist = []
        self.book_id = 1

    def book_registration(self):
        name = input("Enter Book Title: ")

        for book in self.booklist:
            if book["Title"].lower() == name.lower():
                print("Book", book["Title"], "is already registered.")
                return

        author = input("Enter Book Author: ")
        copies = input("Enter Available Copies: ")

        copies = int(copies)

        book = {
            "ID": "B00" +str (self.book_id),
            "Title": name,
            "Author": author,
            "Copies": copies
        }

        self.booklist.append(book)

        print("Book registered successfully.")
        print("Book ID:", book["ID"])

        self.book_id += 1
        
    def view_books(self):

        if len(self.booklist) == 0:
            print("Book Not Registered.")
            return

        for book in self.booklist:
            print("Book ID:", book["ID"])
            print("Book Title:", book["Title"])
            print("Book Author:", book["Author"])
            print("Available Copies:", book["Copies"])

    def update_copies(self):
        book_id = input("Enter Book ID you want to update: ")

        for book in self.booklist:
            if book["ID"].lower() == book_id.lower():
                quantity = input("Enter new available copies: ")

                if not quantity.isdigit():
                    print("Please enter a valid number.")
                    return

                quantity = int(quantity)

                book["Copies"] = quantity

                print("Book", book["Title"], "has been updated to",
                      quantity, "copies.")
                return

        print("Book not found.")

    def borrow_book(self):
        book_id = input("Enter Book ID you want to borrow: ")

        quantity_borrow = input("Enter quantity to borrow: ")

        if not quantity_borrow.isdigit():
            print("Please enter a valid number.")
            return

        quantity_borrow = int(quantity_borrow)

        if quantity_borrow <= 0:
            print("Borrowing quantity must be greater than zero.")
            return

        for book in self.booklist:
            if book["ID"].lower() == book_id.lower():

                if quantity_borrow > book["Copies"]:
                    print("Not enough copies available.")
                    return

                new_copies = book["Copies"] - quantity_borrow
                book["Copies"] = new_copies

                borrowing = {
                    "ID": book_id.upper(),
                    "Quantity": quantity_borrow
                }

                self.borrowlist.append(borrowing)

                print("Book borrowing successful.")
                print("Book Title:", book["Title"])
                print("Quantity Borrowed:", quantity_borrow)
                print("Remaining Copies:", new_copies)
                return

        print("Book not found.")

    def search_book(self):
        book_id = input("Enter Book ID you want to search: ")

        for book in self.booklist:
            if book["ID"].lower() == book_id.lower():
                print("Book ID:", book["ID"])
                print("Book Title:", book["Title"])
                print("Book Author:", book["Author"])
                print("Available Copies:", book["Copies"])
                return

        print("Book not found.")

    def display_summary(self):
        total_books = len(self.booklist)
        total_borrowed = 0

        for borrowing in self.borrowlist:
            total_borrowed += borrowing["Quantity"]

        print("---------------------Library Summary----------------------")
        print("Total number of book titles:", total_books)
        print("Total number of copies borrowed:", total_borrowed)

        print("-----------------Current Available Copies--------------------")

        for book in self.booklist:
            print(book["Title"], "- Available Copies:", book["Copies"])

    def menu_system(self):
        while True:
            print("=================Campus Library Management System=================")
            print("1. Add Book")
            print("2. View All Books")
            print("3. Update Available Copies")
            print("4. Borrow Book")
            print("5. Search Book")
            print("6. View Library Summary")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.book_registration()

            elif choice == "2":
                self.view_books()

            elif choice == "3":
                self.update_copies()

            elif choice == "4":
                self.borrow_book()

            elif choice == "5":
                self.search_book()

            elif choice == "6":
                self.display_summary()

            elif choice == "7":
                print("Thank you for using Campus Library System.")
                break

            else:
                print("Please enter a valid choice.")


lib = LibraryManagement()
lib.menu_system()

lib= LibraryManagement()
lib.book_registration()

##