from django.db import models

# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length=500)

    price = models.IntegerField()

    star_choices = (
        ('1', '*'),
        ('2', '**'),
        ('3', '***'),
        ('4', '****'),
        ('5', '*****')
    )
    rating = models.IntegerField(choices=star_choices)

    is_bestseller = models.BooleanField()

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name