from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Genre
from .serializers.common import GenreSerializer
from .serializers.populated import PopulatedGenreSerializer

class GenreListView(APIView):
  permission_classes = (isAuthenticatedOrReadOnly, )

  def get(self, _request):
    genres = Genre.objects.all()
    serialized_genres = PopulatedGenreSerializer(genres, many=True)
    return Response(serialized_genres.data, status=status.HTTP_200_OK)
  
  def post(self, request):
    genre_to_add = GenreSerializer(data=request.data)
    if genre_to_add.is_valid():
      genre_to_add.save()
      return Response(genre_to_add.data, status=status.HTTP_201_CREATED)

    return Response(genre_to_add.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class GenreDetailView(APIView):
  permission_classes = (isAuthenticatedOrReadOnly, )

  def get_genre(self, pk):
    try:
      return Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
      raise NotFound(detail="Can't find that movie") 
      
  def get(self, _request, pk):
    try:
      genre = Genre.objects.get(pk=pk)
      serialized_genre = PopulatedGenreSerializer(genre)
      return Response(serialized_genre.data, status=status.HTTP_200_OK)
    except Genre.DoesNotExist:
      raise NotFound(detail="Can't find that genre")

  def put(self, request, pk):
      genre_to_update = self.get_genre(pk=pk)
      updated_genre = GenreSerializer(genre_to_update, data=request.data)

      if updated_genre.is_valid():
          updated_genre.save()
          return Response(updated_genre.data, status=status.HTTP_202_ACCEPTED)
      return Response(updated_genre.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
  def delete(self, _request, pk):
      genre_to_delete = self.get_genre(pk=pk)
      genre_to_delete.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)