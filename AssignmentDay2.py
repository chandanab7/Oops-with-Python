
# Learn all 5 types of inheritance and the implementation of single inheritance and multiple inheritance.
# Create a single inheritance program for a Library system.
# Create a parent class named Book with:
# title
# author
# display_book_details() method

# Create a child class named IssuedBook that inherits from Book and adds:
# issued_to
# issued_date
# display_issued_book_details() method
# display_book_details() → shows only title and author
# display_issued_book_details() → shows title, author, issued_to, issued_date

#  (it calls display_book_details() from the parent class using inheritance)


# Create one object of IssuedBook and display all details.
# Push daily progress to GitHub.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book_details(self):
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")

#now child class
class issuedBook(Book):
    def __init__(self, title, author, issued_to, issued_date):
        super().__init__(title, author)  # Call the constructor of the parent class
        self.issued_to = issued_to
        self.issued_date = issued_date

    def display_issued_book_details(self):
        self.display_book_details()  # Call the method from the parent class
        print(f"Issued To: {self.issued_to}")
        print(f"Issued Date: {self.issued_date}")
# Create an object of IssuedBook
issued_book = issuedBook("the girl", "jenny", "anu", "2026-02-4")
# Display all details
issued_book.display_issued_book_details()
