# Use a default value

class Book:
    def __init__(self, title, author, pages=371):
        self.title = title
        self.author = author
        self.pages = pages

book = Book("The Kite Runner", "Khaled Hosseini")
print(book.title, book.author, book.pages)
