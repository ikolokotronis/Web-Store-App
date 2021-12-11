from django.db import models

# Create your models here.


class SubCategoryProduct(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    subcategory = models.ForeignKey('main.SubCategory', on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.subcategory)} --> {self.product}'


class Product(models.Model):

    name = models.CharField(max_length=500)

    producent_name = models.CharField(max_length=250, null=True)

    price = models.IntegerField()

    description = models.TextField(null=True)

    star_choices = (
        ('1', '*'),
        ('2', '**'),
        ('3', '***'),
        ('4', '****'),
        ('5', '*****')
    )
    rating = models.TextField(choices=star_choices)

    is_bestseller = models.BooleanField()

    date_added = models.DateField(auto_now_add=True)

    subcategory_id = models.ManyToManyField('main.SubCategory', through=SubCategoryProduct)

    image = models.ImageField(upload_to='img', null=True)

    def __str__(self):
        return self.name