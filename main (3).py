from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI()

movies = [
{
"id": 1,
"title": "3 Idiots",
"director": "Rajkumar Hirani",
"genre": "Comedy Drama",
"language": "Hindi",
"release_year": 2009
},
{
"id": 2,
"title": "Baahubali",
"director": "S S Rajamouli",
"genre": "Action Drama",
"language": "Telugu",
"release_year": 2015
}
]
class movie_update(BaseModel):
    title:str
    director:str
    genre:str
    language:str
    release_year:int

@app.get("/")
def welcome():
    return {"Message":"API is Running"}

@app.get("/movies")
def fetch_movies():
    return movies

@app.get('/movies/{movie_id}')
def get_movie_by_id(movie_id : int):
    for movie in movies:
        if movie["id"]==movie_id:
            return movie
    raise HTTPException(status_code=404,detail="Movie Not Found !!!")

@app.put('/movies/{movie_id}')
def update_book(movie_id:int,movie:movie_update):
    for existing_movie in movies:
        if existing_movie["id"]==movie_id:

            existing_movie.update(movie.model_dump()) # --- one line did the work of 4
            return{
                "Message":"Movie Updated Succesfully !!!",
                "Movie":existing_movie
            }
    raise HTTPException(status_code=404,detail="Movie Not Found !!!")


