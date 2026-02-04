class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display_book_details(self):
        print("book title is:",self.title)
        print("book author is:",self.author)
class issuedbook(book):
    def __init__(self,title,author,issued_to,issued_date):
        super().__init__(title,author)
        self.issued_to=issued_to
        self.issued_date=issued_date
    def display_issued_book_details(self):
        # self.display_book_details() or
        print("book title is:",self.title)
        print("book author is:",self.author)
        print("issued to:",self.issued_to)
        print("issued date is:",self.issued_date)
object_book=issuedbook("the girl","jenny","anu","2026-02-4")
#object_book.display_issued_book_details()
object_book.display_book_details()