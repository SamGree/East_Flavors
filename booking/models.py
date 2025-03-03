from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Table(models.Model):
    """
    Model representing a table with a specific capacity.
    Orders tables by descending capacity.
    """
    capacity = models.IntegerField()

    class Meta:
        ordering = ('-capacity',)

    def __str__(self):
        return f"Table Capacity: {self.capacity}"


class Booking(models.Model):
    """
    Model representing a booking.
    Includes fields for user, table, date, time, and number of guests.
    """
    GUESTS_CHOICES = [ (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10) ]
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings')
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField(choices=GUESTS_CHOICES, default=1,
                        validators=[MaxValueValidator(10), MinValueValidator(1)])

    def __str__(self):
        return f"Booking for {self.user.username.capitalize()} on {
            self.date} at {self.time} for {self.guests} guests"