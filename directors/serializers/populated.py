from .common import DirectorSerializer
from movies.serializers.common import MovieSerializer
from genres.serializers.common import GenreSerializer
from reviews.serializers.common import ReviewSerializer

class PopulatedDirectorSerializer(DirectorSerializer):
    movie = MovieSerializer()
    genre = GenreSerializer()
    review = ReviewSerializer(many=True)