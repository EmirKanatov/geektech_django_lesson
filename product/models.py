from django.db import models
# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=255)
    category_objects = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Vegetables(models.Model):
    name = models.CharField(max_length=255)
    calories = models.IntegerField(default=0)
    price = models.PositiveIntegerField(default=1)
    is_available = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(to=Categories, null=True,
                                 on_delete=models.SET_NULL, related_name='vegetables')
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Овощи"
        verbose_name_plural = "Овощи"
