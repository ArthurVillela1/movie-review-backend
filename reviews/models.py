from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Review(models.Model):
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    ratings = models.FloatField(
    validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
    )
    movie = models.ForeignKey(
        "movies.Movie",
        related_name = "reviews",
        on_delete=models.CASCADE
    )
    createdby = models.ForeignKey(
        "jwt_auth.User",
        related_name="reviews",
        on_delete = models.CASCADE
    )