# Store the same information in a class

class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating


movie = Movie("Titanic", "James Cameron", 9)
print(movie.title, movie.director, movie.rating)
