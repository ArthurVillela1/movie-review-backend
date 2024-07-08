from .common import GenreSerializer
from movies.serializers.common import movieSerializer
from genres.serializers.common import genreSerializer

class PopulatedDirectorSerializer(DirectorSerializer):
    movie = movieSerializer()
    genre = genreSerializer()