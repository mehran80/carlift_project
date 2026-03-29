from django.db import models
from django.conf import settings
from drivers.models import DriverProfile

class Ride(models.Model):
    CREATOR_ROLE = [
        ('driver', 'Driver'),
        ('passenger', 'Passenger')
    ]

    RIDE_CHOICES = [
        ('private', 'Private'),
        ('shared', 'Shared')
    ]
    
    RIDE_STATUS_CHOICES = {
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    }

    driver = models.ForeignKey(
        DriverProfile,
        on_delete=models.SET_NULL,
        related_name='rides',
        null=True,
        blank= True)
    
    ride_creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        related_name='rides'
        )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    creator_role = models.CharField(max_length=20, choices=CREATOR_ROLE, default = 'passenger')
    ride_status = models.CharField(max_length=20 , choices=RIDE_STATUS_CHOICES, default='pending')
    ride_fare = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ride_type =  models.CharField(max_length=20, choices=RIDE_CHOICES, default='private')
    ride_start_location = models.CharField(max_length=255)
    ride_end_location = models.CharField(max_length=255)
    ride_departure_time = models.DateTimeField()
    ride_departure_date = models.DateField()

    def __str__(self):
        return f"{self.creator_role} Trip: {self.ride_start_location} to {self.ride_end_location}"
