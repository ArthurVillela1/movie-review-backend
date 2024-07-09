from .common import MovieSerializer
from genres.serializers.common import genreSerializer
from directors.serializers.common import directorSerializer
from reviews.serializers.populated import populatedreviewSerializer

class PopulatedMovieSerializer(MovieSerializer):
    genre = genreSerializer()
    director = directorSerializer()
    review = populatedReviewSerializer(many=True)