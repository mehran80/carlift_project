from django.db import models
from drivers.models import DriverProfile

class Car(models.Model):
    driver = models.OneToOneField('drivers.DriverProfile', on_delete=models.CASCADE, related_name='car')
    car_registration_paper_pic = models.ImageField(
        upload_to='car_registration_paper_pic/',
        blank=False,
        null=False,
        default='car_registration_paper_pic/default.png'
        )
    car_pic = models.ImageField(
        upload_to='car_pic/',
        blank=False,
        null=False,
        default='car_pic/default.png'
        )
    car_maker = models.CharField(max_length=50, help_text="Example: Toyota")
    car_model = models.CharField( max_length=50, help_text="Example: Toyota")
    car_model_year = models.PositiveIntegerField(help_text="Example: 2022")
    car_seat_capacity = models.PositiveBigIntegerField(default=4, help_text="Example: 5")
    car_color = models.CharField(max_length=20)
    car_plate_number = models.CharField(max_length=20,unique=True, help_text="Example: Y36565")

    def __str__(self) -> str:
        return f"{self.car_maker} {self.car_model} ({self.car_plate_number})"
