from django.contrib import admin
from .models import Category, SubCategory, CategorySubCategory, Order
# Register your models here.

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(CategorySubCategory)
admin.site.register(Order)