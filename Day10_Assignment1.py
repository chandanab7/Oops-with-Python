class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book: {self.title} by {self.author} costs ₹{self.price}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.price})"


b1 = Book("Python Basics", "John", 499)
b2 = Book("AI Guide", "Smith", 699)

print(b1)          # Calls __str__()
print([b1, b2])    # Calls __repr__()
