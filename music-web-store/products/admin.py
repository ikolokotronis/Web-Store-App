from django.contrib import admin
from .models import Product, SubCategoryProduct

admin.site.register(Product)
admin.site.register(SubCategoryProduct)