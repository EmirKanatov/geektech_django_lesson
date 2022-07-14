from django.db import models


# Create your models here.
class Vegetables(models.Model):
    name = models.CharField(max_length=255)
    calories = models.IntegerField(default=0)
    price = models.PositiveIntegerField(default=1)
    is_available = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    objects = models.Manager()


class Categories(models.Model):
    name = models.CharField(max_length=255)
    category_objects = models.CharField(max_length=255)
    objects = models.Manager()
