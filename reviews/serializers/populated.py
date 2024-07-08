from .common import ReviewSerializer
from genres.serializers.common import genreSerializer
from directors.serializers.common import directorSerializer
from movies.serializers.common import movieSerializer

class PopulatedReviewSerializer(ReviewSerializer):
    genre = genreSerializer()
    director = directorSerializer()
    movie = movieSerializer()
