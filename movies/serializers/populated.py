from .common import MovieSerializer
from genres.serializers.common import genreSerializer

class PopulatedMovieSerializer(MovieSerializer):
    genre = genreSerializer()