from rest_framework.views import APIView # this imports rest_frameworks APIView that we'll use to extend to our custom view
from rest_framework.response import Response # Response gives us a way of sending a http response to the user making the request, passing back data and other information
from rest_framework import status # status gives us a list of official/possible response codes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Director
from .serializers.common import DirectorSerializer
# from .serializers.populated import PopulatedDirectorSerializer

class DirectorListView(APIView):
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
# custom method to retrieve a book from the DB and error if it's not found
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