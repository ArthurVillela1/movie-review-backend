from rest_framework.views import APIView # this imports rest_frameworks APIView that we'll use to extend to our custom view
from rest_framework.response import Response # Response gives us a way of sending a http response to the user making the request, passing back data and other information
from rest_framework import status # status gives us a list of official/possible response codes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Movie
from .serializers.common import MovieSerializer
# from .serializers.populated import PopulatedMovieSerializer

class MovieListView(APIView):
  def get(self, _request):
    movies = Movie.objects.all()
    serialized_movies = MovieSerializer(movies, many=True)
    return Response(serialized_movies.data, status=status.HTTP_200_OK)
  
  def post(self, request):
    movie_to_add = MovieSerializer(data=request.data)
    if movie_to_add.is_valid():
      movie_to_add.save()
      return Response(movie_to_add.data, status=status.HTTP_201_CREATED)

    return Response(movie_to_add.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

