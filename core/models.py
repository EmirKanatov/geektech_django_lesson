from django.db import models

# Create your models here.


class Feedback(models.Model):
    first_name = models.CharField(max_length=255)
    rating = models.IntegerField(default=10)
    text = models.TextField(null=True, blank=True)
    contact = models.CharField(max_length=255, verbose_name="Номер или почта для связи")