from django.db import models
from django.contrib.auth.models import User


class Table(models.Model):
    capacity = models.IntegerField()

    class Meta:
        ordering = ('-capacity',)

    def __str__(self):
        return f"Table Capacity: {self.capacity}"


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings')
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()

    def __str__(self):
        return f"Booking for {self.user.username.capitalize()} on {self.date} at {self.time} for {self.guests} guests"
