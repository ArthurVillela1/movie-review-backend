from django.db import models

# Create your models here.

class Movie(models.Model):
    def __str__(self):
        return f'{self.name}'
    name = models.CharField(max_length=80, unique=True)
    genre = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    releaseDate = models.FloatField()

    