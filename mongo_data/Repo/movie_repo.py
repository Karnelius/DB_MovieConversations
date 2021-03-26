from mongo_data.Models.movies import Movie


def store_movies(lines):
    for line in lines:
        movie = Movie(**line)
        movie.save()

