from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    ROLE_CHOICES = (
        ('passenger','Passenger'),
        ('driver', 'Driver'),
    )

    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='passenger')
    phone_number = PhoneNumberField(
        unique=True,
        blank=False,
        null=False,
        help_text="Enter number with country code (e.g. +971501234567)"
        )
    email =  models.CharField(max_length=200, unique=True, blank=False, null=False)
    profile_image = models.ImageField(
        blank=True,
        null=True, 
        upload_to='profile_pics/',
        default='profile_pics/default.png'
        )
    

    @property
    def is_driver(self):
        return self.role == 'driver'
    

    @property
    def is_passenger(self):
        return self.role == 'passenger'
    
    def __str__(self):
        return f"{self.pk}"