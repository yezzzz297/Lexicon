
catalogue = [
    {
        "id": "M001",
        "title": "Titanic",
        "type": "movie",
        "genre": "Romance",
        "year": 1997
    },
    {
        "id": "M002",
        "title": "Harry Potter",
        "type": "movie",
        "genre": "Fantasy",
        "year": 2001
    },
    {
        "id": "M003",
        "title": "The Handmaid's Tale",
        "type": "movie",
        "genre": "Drama",
        "year": 1990
    }
]

print(catalogue[0]["title"])
print(catalogue[0]["type"])
print(catalogue[0]["genre"])
print(catalogue[0]["year"])

catalogue[2]["genre"] = "Dystopian"
print(catalogue[2]["genre"])
print(catalogue[1]["id"])

catalogue.pop(1)
print(len(catalogue))
print("movie" in catalogue[0].values())
print(catalogue[-1]["title"])
