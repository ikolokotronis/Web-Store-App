from django.db import models
from users.models import WebsiteUser
from products.models import Product


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.name


class CategorySubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category}->{self.subcategory}'


class SubCategory(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    category_id = models.ManyToManyField(Category, through=CategorySubCategory)

    def __str__(self):
        return self.name


class ShoppingCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(WebsiteUser, on_delete=models.CASCADE)
    quantity = models.IntegerField()