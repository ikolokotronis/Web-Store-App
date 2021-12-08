from django.shortcuts import render
from django.views import View
from main.models import Category
from products.models import Product
# Create your views here.


class ProductView(View):
    def get(self, request, product_id):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        product = Product.objects.get(id=product_id)
        return render(request, 'product/product_details.html', {'stringed_instruments': stringed_instruments,
                                                  'keyboard_instruments': keyboard_instruments,
                                                  'drums': drums,
                                                  'sound_system': sound_system,
                                                  'product': product}
                      )