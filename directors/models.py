from django.db import models

# Create your models here.

class Director(models.Model):
   def __str__(self):
     return f'{self.name}'

   name = models.TextField(max_length=35)
