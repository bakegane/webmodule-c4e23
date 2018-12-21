import mlab
from models.user import User
from models.movie import Movie


mlab.connect()

# Movie.drop_collection()
for movie in Movie.objects():
    print(movie.title)
    print(movie.user.username)