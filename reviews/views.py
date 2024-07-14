from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Review
from .serializers.common import ReviewSerializer
from .serializers.populated import PopulatedReviewSerializer
from rest_framework.exceptions import ValidationError

class ReviewListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def post(self, request):
        user = request.user
        movie_id = request.data.get('movie')

        # Check if the user has already reviewed the movie
        if Review.objects.filter(owner=user, movie_id=movie_id).exists():
            raise ValidationError("You have already reviewed this movie.")

        # Proceed with creating the review if not already reviewed
        request.data["owner"] = user.id
        review_to_add = ReviewSerializer(data=request.data)
        if review_to_add.is_valid():
            review_to_add.save()
            return Response(review_to_add.data, status=status.HTTP_201_CREATED)
        return Response(review_to_add.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
class ReviewDetailView(APIView):
  permission_classes = (IsAuthenticatedOrReadOnly, )

  def get_review(self, pk):
    try:
      return Review.objects.get(pk=pk)
    except Review.DoesNotExist:
      raise NotFound(detail="Can't find that review") 
      
  def get(self, _request, pk):
    try:
      review = Review.objects.get(pk=pk)
      serialized_review = PopulatedReviewSerializer(review)
      return Response(serialized_review.data, status=status.HTTP_200_OK)
    except Review.DoesNotExist:
      raise NotFound(detail="Can't find that review")

  def put(self, request, pk):
      review_to_update = self.get_review(pk=pk)

      if review_to_update.owner != request.user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

      updated_review = ReviewSerializer(review_to_update, data=request.data)
      if updated_review.is_valid():
          updated_review.save()
          return Response(updated_review.data, status=status.HTTP_202_ACCEPTED)
      return Response(updated_review.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
  def delete(self, _request, pk):
      review_to_delete = self.get_review(pk=pk)
      review_to_delete.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)