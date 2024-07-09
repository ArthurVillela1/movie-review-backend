from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Director
from .serializers.common import DirectorSerializer

class DirectorListView(APIView):
  permission_classes = (isAuthenticatedOrReadOnly, )

  def get(self, _request):
    directors = director.objects.all()
    serialized_directors = DirectorSerializer(directors, many=True)
    return Response(serialized_directors.data, status=status.HTTP_200_OK)
  
  def post(self, request):
    director_to_add = DirectorSerializer(data=request.data)
    if director_to_add.is_valid():
      director_to_add.save()
      return Response(director_to_add.data, status=status.HTTP_201_CREATED)

    return Response(director_to_add.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class DirectorDetailView(APIView):
  permission_classes = (isAuthenticatedOrReadOnly, )

  def get_director(self, pk):
    try:
      return Director.objects.get(pk=pk)
    except Director.DoesNotExist:
      raise NotFound(detail="Can't find that director") 
      
  def get(self, _request, pk):
    try:
      director = Director.objects.get(pk=pk)
      serialized_director = DirectorSerializer(director)
      return Response(serialized_director.data, status=status.HTTP_200_OK)
    except Director.DoesNotExist:
      raise NotFound(detail="Can't find that director")

  def put(self, request, pk):
      director_to_update = self.get_director(pk=pk)
      updated_director = DirectorSerializer(director_to_update, data=request.data)

      if updated_director.is_valid():
          updated_director.save()
          return Response(updated_director.data, status=status.HTTP_202_ACCEPTED)
      return Response(updated_director.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
  def delete(self, _request, pk):
      director_to_delete = self.get_director(pk=pk)
      director_to_delete.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)