from django.db import models

class Movie(models.Model):
    def __str__(self):
        return f'{self.name}'
    #isAdmin = models.Bolean(default=False)
    name = models.CharField(max_length=80, unique=True)
    poster = models.CharField(max_length=500)
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