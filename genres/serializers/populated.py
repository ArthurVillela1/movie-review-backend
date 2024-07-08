from .common import GenreSerializer
from movies.serializers.common import movieSerializer

class PopulatedGenreSerializer(GenreSerializer):
    movie = movieSerializer()