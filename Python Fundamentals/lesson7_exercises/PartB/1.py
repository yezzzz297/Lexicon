# Check whether a book is long

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        return self.pages > 300

book1 = Book("The Kite Runner", "Khaled Hosseini", 371)
book2 = Book("The Housemaid", "Freida McFadden", 336)
print(book1.title, book1.is_long())
print(book2.title, book2.is_long())
