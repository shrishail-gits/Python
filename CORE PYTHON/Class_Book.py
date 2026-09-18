class Book:

    # Class variable
    library_name = "City Library"

    # Constructor
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # Instance method
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Library:", Book.library_name)

    # Class method
    @classmethod
    def change_library(cls, new_name):
        cls.library_name = new_name

    # Static method
    @staticmethod
    def validate_price(price):
        return price > 0

# Creating object
b1 = Book("Python Programming", "John Smith", 800)
b1.display()
print("Valid Price:", Book.validate_price(800))
Book.change_library("Central Library")
print("\nAfter changing library name:")
b1.display()