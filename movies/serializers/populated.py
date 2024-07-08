from .common import MovieSerializer
from genres.serializers.common import genreSerializer
from directors.serializers.common import directorSerializer

class PopulatedMovieSerializer(MovieSerializer):
    genre = genreSerializer()
    director = directorSerializer()