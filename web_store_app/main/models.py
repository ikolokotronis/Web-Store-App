from django.db import models
from users.models import WebsiteUser
from products.models import Product


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class ShoppingCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(WebsiteUser, on_delete=models.CASCADE)
    quantity = models.IntegerField()