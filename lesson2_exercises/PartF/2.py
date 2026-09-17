# Part F/2: Create the catalogue list

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

print("Catalogue entries:", len(catalogue))
print(catalogue[0]["title"], catalogue[0]["type"])
