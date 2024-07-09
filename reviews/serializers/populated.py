from .common import ReviewSerializer
from genres.serializers.common import GenreSerializer
from directors.serializers.common import DirectorSerializer
from movies.serializers.common import MovieSerializer
from jwt_auth.serializers import UserSerializer

class PopulatedReviewSerializer(ReviewSerializer):
    genre = GenreSerializer()
    director = DirectorSerializer()
    movie = MovieSerializer()
    owner = UserSerializer()