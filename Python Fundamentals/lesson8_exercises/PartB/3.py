# Check the rating

class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def is_highly_rated(self):
        # Example ratings use a scale from 0 to 10.
        if self.rating >= 8:
            return True
        return False


movie = Movie("Titanic", "James Cameron", 9)
print(movie.title, movie.director, movie.rating)


print(movie.is_highly_rated())
