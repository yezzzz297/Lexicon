# Part E/3: Change one nested value and add one new key

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

books[0]["available"] = False
books[0]["genre"] = "Romance"

print(books[0]["title"])
print(books[0]["available"])
print(books[0]["genre"])
