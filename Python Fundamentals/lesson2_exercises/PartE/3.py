# Part E/3: Change one nested value and add one new key

books = [
    {
        "title": "The Kite Runner",
        "author": "Khaled Hosseini",
        "pages": 371,
        "available": True
    },
    {
        "title": "It Ends with Us",
        "author": "Colleen Hoover",
        "pages": 384,
        "available": True
    },
    {
        "title": "The Housemaid",
        "author": "Freida McFadden",
        "pages": 336,
        "available": False
    },
    {
        "title": "A Thousand Splendid Suns",
        "author": "Khaled Hosseini",
        "pages": 432,
        "available": True
    }
]

books[0]["available"] = False
books[0]["genre"] = "Historical Fiction"

print(books[0]["title"])
print(books[0]["available"])
print(books[0]["genre"])
