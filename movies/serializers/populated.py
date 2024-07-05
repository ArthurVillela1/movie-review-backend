from .common import MovieSerializer
#from reviews.serializers.common import ReviewSerializer
#from ratings.serializers import RatingSerializer

class PopulatedMovieSerializer(MovieSerializer):
  review = "ReviewSerializer()"
  ratings = "RatingSerializer(many=True)"