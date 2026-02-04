
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

# Create one object of IssuedBook and display all details.
# Push daily progress to GitHub.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book_details(self):
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")

# now child class
class IssuedBook(Book):
    def __init__(self, title, author, issued_to, issued_date):
        super().__init__(title, author)
        self.issued_to = issued_to
        self.issued_date = issued_date

    def display_issued_book_details(self):  #  (it calls display_book_details() from the parent class using inheritance)
        self.display_book_details()
        print(f"Issued To: {self.issued_to}")
        print(f"Issued Date: {self.issued_date}")
# Create an object of IssuedBook
issued_book = IssuedBook("the girl", "jenny", "anu", "2026-02-4")
# Display all details
issued_book.display_issued_book_details()
# Output:
# Book Title:
