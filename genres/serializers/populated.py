from .common import GenreSerializer
from movies.serializers.common import movieSerializer
from directors.serializers.common import directorSerializer
from reviews.serializers.common import reviewSerializer

class PopulatedGenreSerializer(GenreSerializer):
    movie = movieSerializer()
    director = directorSerializer()
    review = reviewSerializer()