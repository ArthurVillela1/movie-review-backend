from rest_framework.views import APIView # this imports rest_frameworks APIView that we'll use to extend to our custom view
from rest_framework.response import Response # Response gives us a way of sending a http response to the user making the request, passing back data and other information
from rest_framework import status # status gives us a list of official/possible response codes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Movie
from .serializers.common import MovieSerializer
from .serializers.populated import PopulatedMovieSerializer

class MovieListView(APIView):
  permission_classes = (IsAuthenticatedOrReadOnly, )
  def get(self, _request):
    # go to the database and get all the books
    movies = Movie.objects.all()
    # translate the books from the database to a usable form
    serialized_movies = MovieSerializer(movies, many=True)
    # return the serialized data and a 200 status code
    return Response(serialized_movies.data, status=status.HTTP_200_OK)

  def post(self, request):
    movie_to_add = MovieSerializer(data=request.data)
    try:
      movie_to_add.is_valid()
      movie_to_add.save()
      return Response(movie_to_add.data, status=status.HTTP_201_CREATED)
    except Exception as e:
      print("Error")
      # the below is necessary because two different formats of errors are possible. string or object format.
      # if it's string then e.__dict__ returns an empty dict {}
      # so we'll check it's a dict first, and if it's empty (falsey) then we'll use str() to convert to a string            
      return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class MovieDetailView(APIView):
# custom method to retrieve a book from the DB and error if it's not found
  def get_movie(self, pk):
    try:
      return Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
      raise NotFound(detail="Can't find that movie") 
      
  def get(self, _request, pk):
    try:
      movie = Movie.objects.get(pk=pk)
      serialized_movie = PopulatedMovieSerializer(movie)
      return Response(serialized_movie.data, status=status.HTTP_200_OK)
    except Movie.DoesNotExist:
      raise NotFound(detail="Can't find that movie")

