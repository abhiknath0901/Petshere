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
    
class Address(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    receiver_name = models.CharField(max_length=255)
    receiver_phone = models.CharField(max_length=20)
    pincode = models.CharField(max_length=20)

    house_no_or_name = models.CharField(max_length=255)
    street_area_locality = models.CharField(max_length=255)

    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    landmark = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.receiver_name} - {self.city}"

class Order(models.Model):

    STATUS_CHOICES = [

        ('pending', 'Pending'),

        ('confirmed', 'Confirmed'),

        ('shipped', 'Shipped'),

        ('delivered', 'Delivered'),

        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
    )

    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_method = models.CharField(

        max_length=30,

        choices=[

            ('card', 'Card'),

            ('upi', 'UPI'),

            ('netbanking', 'Net Banking'),

            ('cod', 'Cash on Delivery'),
        ],

        default='card'
    )

    payment_status = models.CharField(

        max_length=30,

        choices=[

            ('pending', 'Pending'),

            ('paid', 'Paid'),

            ('failed', 'Failed'),
        ],

        default='pending'
    )

    razorpay_order_id = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

   
    razorpay_payment_id = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default='pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"Order #{self.id}"

class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.pet.name} x {self.quantity}"