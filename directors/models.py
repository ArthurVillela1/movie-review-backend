from django.db import models

class Director(models.Model):
   def __str__(self):
     return f'{self.name}'

   name = models.TextField(max_length=35)
