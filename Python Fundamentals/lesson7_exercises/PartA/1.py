# Create four books

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

books = [
    Book("The Kite Runner", "Khaled Hosseini", 371),
    Book("It Ends with Us", "Colleen Hoover", 384),
    Book("The Housemaid", "Freida McFadden", 336),
    Book("A Thousand Splendid Suns", "Khaled Hosseini", 432),
]
for book in books:
    print(book.title, book.author, book.pages)
