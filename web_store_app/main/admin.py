from django.contrib import admin
from .models import Category, SubCategory, CategorySubCategory, Order, ProductOrder, Complaint, DiscountCodes

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(CategorySubCategory)
admin.site.register(Order)
admin.site.register(ProductOrder)
admin.site.register(Complaint)
admin.site.register(DiscountCodes)