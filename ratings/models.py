from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Rating(models.Model):
    percentage = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    movie = models.ForeignKey(
        "movies.Movie",
        related_name = "ratings",
        on_delete=models.CASCADE
    )
    createdby = models.ForeignKey(
        "jwt_auth.User",
        related_name="ratings",
        on_delete = models.CASCADE
    )