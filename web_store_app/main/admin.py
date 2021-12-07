from django.contrib import admin
from .models import Category, SubCategory, ShoppingCart
# Register your models here.

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ShoppingCart)