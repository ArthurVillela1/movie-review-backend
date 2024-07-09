from .common import GenreSerializer
from movies.serializers.common import MovieSerializer
from directors.serializers.common import DirectorSerializer
from reviews.serializers.common import ReviewSerializer

class PopulatedGenreSerializer(GenreSerializer):
    movie = MovieSerializer()
    director = DirectorSerializer()
    review = ReviewSerializer(many=True)