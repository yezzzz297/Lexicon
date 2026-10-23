import json
import os
from fastapi import FastAPI, HTTPException, Header, Depends, Response
from pydantic import BaseModel
from dotenv import load_dotenv

folder = os.path.dirname(__file__)
load_dotenv(os.path.join(folder, ".env"))
API_KEY = os.getenv("API_KEY")
DATA_FILE = os.path.join(folder, "movies.json")

app = FastAPI()


class Movie(BaseModel):
    title: str
    director: str
    year: int


class MovieUpdate(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None


def load_movies():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as file:
            return json.load(file)
    return [
        {"id": 1, "title": "Alien", "director": "Ridley Scott", "year": 1979},
        {"id": 2, "title": "The Matrix", "director": "The Wachowskis", "year": 1999},
        {"id": 3, "title": "Gladiator", "director": "Ridley Scott", "year": 2000},
        {"id": 4, "title": "Inception", "director": "Christopher Nolan", "year": 2010},
    ]


movies = load_movies()


def save_movies():
    with open(DATA_FILE, "w") as file:
        json.dump(movies, file, indent=2)


def find_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


def check_key(x_api_key: str | None = Header(default=None)):
    if not API_KEY or x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Missing or wrong API key")


@app.get("/movies")
def get_movies(director: str | None = None, year: int | None = None):
    result = movies
    if director is not None:
        result = [movie for movie in result if director.lower() in (movie["director"] or "").lower()]
    if year is not None:
        result = [movie for movie in result if movie["year"] == year]
    return result


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    return find_movie(movie_id)


@app.post("/movies", status_code=201, dependencies=[Depends(check_key)])
def add_movie(movie: Movie):
    next_id = max((item["id"] for item in movies), default=0) + 1
    new_movie = {"id": next_id, **movie.model_dump()}
    movies.append(new_movie)
    save_movies()
    return new_movie


# Use PUT when replacing a movie with all its fields.
# Use PATCH when changing only selected fields and keeping the others.
@app.put("/movies/{movie_id}", dependencies=[Depends(check_key)])
def replace_movie(movie_id: int, movie: Movie):
    existing = find_movie(movie_id)
    existing.update(movie.model_dump())
    save_movies()
    return existing


@app.patch("/movies/{movie_id}", dependencies=[Depends(check_key)])
def update_movie(movie_id: int, changes: MovieUpdate):
    movie = find_movie(movie_id)
    movie.update(changes.model_dump(exclude_unset=True))
    save_movies()
    return movie


@app.delete("/movies/{movie_id}", status_code=204, dependencies=[Depends(check_key)])
def delete_movie(movie_id: int):
    movie = find_movie(movie_id)
    movies.remove(movie)
    save_movies()
    return Response(status_code=204)


# Two simultaneous changes could overwrite each other or damage the JSON file.
# Databases use transactions and locking to keep concurrent changes consistent.
