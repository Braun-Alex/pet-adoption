from django.db import models

# Create your models here.

from animal.models import Animal  # Импортируйте модель Animal

class User(models.Model):
    name = models.CharField(max_length=100)
    owned_animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

