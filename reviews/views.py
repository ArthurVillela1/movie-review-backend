from rest_framework.views import APIView # this imports rest_frameworks APIView that we'll use to extend to our custom view
from rest_framework.response import Response # Response gives us a way of sending a http response to the user making the request, passing back data and other information
from rest_framework import status # status gives us a list of official/possible response codes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Review
from .serializers.common import ReviewSerializer
# from .serializers.populated import PopulatedReviewSerializer

class ReviewListView(APIView):
  def get(self, _request):
    ewviews = Review.objects.all()
    serialized_reviews = ReviewSerializer(reviews, many=True)
    return Response(serialized_reviews.data, status=status.HTTP_200_OK)
  
  def post(self, request):
    review_to_add = ReviewSerializer(data=request.data)
    if review_to_add.is_valid():
      review_to_add.save()
      return Response(review_to_add.data, status=status.HTTP_201_CREATED)

    return Response(review_to_add.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class ReviewDetailView(APIView):
# custom method to retrieve a book from the DB and error if it's not found
  def get_review(self, pk):
    try:
      return Review.objects.get(pk=pk)
    except Review.DoesNotExist:
      raise NotFound(detail="Can't find that review") 
      
  def get(self, _request, pk):
    try:
      review = Review.objects.get(pk=pk)
      serialized_review = ReviewSerializer(review)
      return Response(serialized_review.data, status=status.HTTP_200_OK)
    except Review.DoesNotExist:
      raise NotFound(detail="Can't find that review")

  def put(self, request, pk):
      mreview_to_update = self.get_review(pk=pk)
      updated_review = ReviewSerializer(review_to_update, data=request.data)

      if updated_review.is_valid():
          updated_review.save()
          return Response(updated_review.data, status=status.HTTP_202_ACCEPTED)
      return Response(updated_review.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
  def delete(self, _request, pk):
      review_to_delete = self.get_review(pk=pk)
      review_to_delete.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)