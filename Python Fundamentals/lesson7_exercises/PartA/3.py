# Check whether two objects are the same object

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book1 = Book("The Kite Runner", "Khaled Hosseini", 371)
book2 = Book("The Kite Runner", "Khaled Hosseini", 371)
print("Same object:", book1 is book2)
