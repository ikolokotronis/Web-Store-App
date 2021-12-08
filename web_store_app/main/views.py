from django.shortcuts import render
from django.views import View
from .models import Category, SubCategory
from products.models import Product
from datetime import date, timedelta
# Create your views here.


class HomePageView(View):
    def get(self, request):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        all_categories = Category.objects.all()
        bestsellers = Product.objects.filter(is_bestseller=True)
        added_recently = Product.objects.filter(date_added__gte=date.today() - timedelta(days=3), date_added__lte=date.today())
        return render(request, 'main/base.html', {'stringed_instruments': stringed_instruments,
                                                  'keyboard_instruments': keyboard_instruments,
                                                  'drums': drums,
                                                  'sound_system': sound_system,
                                                  'bestsellers': bestsellers,
                                                  'added_recently': added_recently,
                                                  'all_categories': all_categories}
                      )


class CategoryDetailsView(View):
    def get(self, request, category_id):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        subcategories = SubCategory.objects.filter(category_id=category_id)
        return render(request, 'main/category_details.html', {'stringed_instruments': stringed_instruments,
                                                                'keyboard_instruments': keyboard_instruments,
                                                                'drums': drums,
                                                                'sound_system': sound_system,
                                                                'subcategories': subcategories}
                      )