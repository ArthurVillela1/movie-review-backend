from .common import DirectorSerializer
from movies.serializers.common import movieSerializer
from genres.serializers.common import genreSerializer
from reviews.serializers.common import reviewSerializer

class PopulatedDirectorSerializer(DirectorSerializer):
    movie = movieSerializer()
    genre = genreSerializer()
    review = reviewSerializer()