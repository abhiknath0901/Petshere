from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import UserProfileManager


# Create your models here.

class UserProfile(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        
        return self.email

class Pet(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    price = models.IntegerField()
    breed_info = models.CharField()
    img = models.ImageField(upload_to='pets/')
    desc = models.CharField()
    health = models.CharField()
    behavior = models.CharField()
    care = models.CharField()
    extra = models.CharField()
    seller = models.CharField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.email} - {self.pet.name} (Quantity: {self.quantity})"
    
class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.user.email} for {self.pet.name} (Quantity: {self.quantity})"