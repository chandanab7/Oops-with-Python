# task 5
class Calculator:
    def __call__(self, a, b):
        return a + b


obj = Calculator()
print(obj(10, 20))



# task 6
class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value


cart = ShoppingCart(["Shoes", "Bag", "Watch"])

print(cart[0])          # Shoes
cart[1] = "Laptop"
print(cart.items)


#task 7
class Session:
    def __del__(self):
        print("Session Ended")


s = Session()
del s


#task 8
class Library:
    def __init__(self, books):
        self.books = books

    def __contains__(self, item):
        return item in self.books


library = Library(["Python", "Java", "C++"])

print("Python" in library)   # True
print("AI" in library)       # False


#task 9
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary


e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)

print(e1 > e2)   # False
print(e1 < e2)   # True


#task 10
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


for i in Counter(1, 5):
    print(i)
