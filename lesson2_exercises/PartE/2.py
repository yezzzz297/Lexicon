# Part E/2: Access a book title and availability

books = [
    {
        "title": "Love Story",
        "author": "Anna Green",
        "pages": 544,
        "available": True
    },
    {
        "title": "The Heart",
        "author": "Robert Brown",
        "pages": 464,
        "available": True
    },
    {
        "title": "Forever Us",
        "author": "Al Smith",
        "pages": 592,
        "available": False
    },
    {
        "title": "The Last Promise",
        "author": "David Stone",
        "pages": 352,
        "available": True
    },
    {
        "title": "Love and Light",
        "author": "Luciano Rose",
        "pages": 1012,
        "available": False
    }
]

print(books[2]["title"])
print(books[-1]["available"])
