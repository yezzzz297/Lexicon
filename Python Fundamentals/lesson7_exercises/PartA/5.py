# Use keyword arguments

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book = Book(title="The Kite Runner", author="Khaled Hosseini", pages=371)
print(book.title, book.author, book.pages)
