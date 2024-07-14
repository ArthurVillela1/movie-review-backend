from rest_framework import serializers
from ..models import Movie

class MovieSerializer(serializers.ModelSerializer):
  average_rating = serializers.FloatField(read_only=True)
  class Meta:
    model = Movie
    fields = '__all__'
