class Book:
    def __init__(self, tittle, author_name, copies_available):
        self.tittle = tittle
        self.author_name = author_name
        self.copies_available = copies_available

    def display_book(self):
        print("Tittle of the Book: ",self.tittle)
        print("Author Name: ",self.author_name)
        print("Number of Copies: ",self.copies_available)

    def borrow_book(self, amount):
        if amount <= self.copies_available:
            self.copies_available =self.copies_available -  amount
            print("Book borrowed successfully")
        else:
            print("Sorry, No copies available")

    def return_book(self , amount):
        self.copies_available = self.copies_available + amount
        print("Book Returned successfully")

book1 = Book("In The Night No Control", "Sandip Bhatta", 500)
book1.display_book()
book1.borrow_book(50)
book1.return_book(7)
book1.display_book()