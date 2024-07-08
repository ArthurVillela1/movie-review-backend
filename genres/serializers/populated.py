from .common import GenreSerializer
from movies.serializers.common import movieSerializer
from directors.serializers.common import directorSerializer

class PopulatedGenreSerializer(GenreSerializer):
    movie = movieSerializer()
    director = directorSerializer()