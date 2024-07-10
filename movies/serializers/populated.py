from .common import MovieSerializer
from genres.serializers.common import GenreSerializer
from directors.serializers.common import DirectorSerializer
from reviews.serializers.populated import PopulatedReviewSerializer

class PopulatedMovieSerializer(MovieSerializer):
    genre = GenreSerializer()
    director = DirectorSerializer()
    #review = PopulatedReviewSerializer(many=True)