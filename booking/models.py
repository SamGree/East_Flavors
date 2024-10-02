from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField()

    def __str__(self):
        return f"Reservation for {self.user.username} on {self.date} at {self.time}"



# Create your models here.
