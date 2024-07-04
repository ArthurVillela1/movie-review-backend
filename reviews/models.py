from django.db import models

# Create your models here.

class Review(models.Model):
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey(
        "movies.Movie",
        related_name = "comments",
        on_delete=models.CASCADE
    )