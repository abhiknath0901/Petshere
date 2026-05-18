from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

    
class Pet(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    price = models.IntegerField()
    breed_info = models.CharField()
    img = models.ImageField(upload_to='pets/')
    description = models.CharField()
    health = models.CharField()
    behavior = models.CharField()
    care = models.CharField()
    extra = models.CharField()
    seller = models.CharField()

    def __str__(self):
        return self.name
