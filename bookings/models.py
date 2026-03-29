from django.db import models
from django.conf import settings
from rides.models import Ride

class Booking(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='bookings')
    passenger = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings'
        )
    
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    booking_time = models.DateTimeField(auto_now_add=True)
    booking_date = models.DateField(auto_now_add=True)
    seat_reserved = models.PositiveIntegerField(default=1)
    is_confirmed = models.BooleanField(default=False)
    passenger_contact_number = models.CharField(max_length=20, blank=True, null=True)
