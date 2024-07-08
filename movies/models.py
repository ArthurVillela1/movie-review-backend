from django.db import models

# Create your models here.

class Movie(models.Model):
    def __str__(self):
        return f'{self.name}'
    name = models.CharField(max_length=80, unique=True)
    releaseDate = models.FloatField()
    genre = models.ForeignKey(
        'genres.Genre',
        related_name='movies',
        on_delete=models.CASCADE
    )
    director = models.ForeignKey(
        'directors.Director',
        related_name='movies',
        on_delete=models.CASCADE
    )