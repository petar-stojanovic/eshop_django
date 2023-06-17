from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Component(models.Model):
    PLATFORM_CHOICES = [
        ('desktop', 'Desktop'),
        ('laptop', 'Laptop'),
    ]

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES, default="desktop")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return self.name
