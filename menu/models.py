from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu-images/', null=True, blank=True)

    def __str__(self):
        return self.name

