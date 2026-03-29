from django.db import models
from decimal import Decimal
from accounts.models import User

class DriverProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver_proffile')

    license_number = models.CharField(max_length=50, unique=True, blank=False, null=False)
    license_expiry = models.DateField(null=False, blank=False, auto_now=False, auto_now_add=False)
    is_verified = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=Decimal(5.00))
    license_image = models.ImageField(
        blank=False,
        null=False,
        upload_to='license_images/',
        default='license_images/default.png'
        )
    last_active = models.DateTimeField(auto_now=True)

    def __str__(self):
        status = "online" if self.is_online else "ofline"
        return f"{self.user.username}-{status}"

