from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Menu(models.Model):
    """
    Represents a menu item in the restaurant, including name,
    description, price, and an optional image field.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField(
        'image',
        default='placeholder', null=True, blank=True)


def __str__(self):
    return self.name
