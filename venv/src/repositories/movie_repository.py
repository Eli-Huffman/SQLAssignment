from src.models import Movie, db

class MovieRepository:

    def get_all_movies(self):
        all_movies = movie_repository_singleton.get_all_movies()
        return None

    def get_movie_by_id(self, movie_id):
        single_movie = movie_repository_singleton.get_movie_by_id(movie_id)
        return None

    def create_movie(self, title, director, rating):
        title = title.form.get('title', '')
        director = director.form.get('director', '')
        rating = rating.form.get('rating', 0, type=int)
        if title == '' or director == '' or rating < 1 or rating > 5:
            return None

    def search_movies(self, title):
        q = title.args.get('q', '')
        if q != '':
            return None


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
