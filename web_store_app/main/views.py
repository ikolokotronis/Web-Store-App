from django.shortcuts import render
from django.views import View
from .models import Category, SubCategory, CategorySubCategory
from products.models import Product
from datetime import date, timedelta
# Create your views here.


class HomePageView(View):
    def get(self, request):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        all_categories = SubCategory.objects.all()
        bestsellers = Product.objects.filter(is_bestseller=True)[0:3]
        added_recently = Product.objects.filter(date_added__gte=date.today() - timedelta(days=3),
                                                date_added__lte=date.today())[0:3]
        return render(request, 'main/base.html', {'stringed_instruments': stringed_instruments,
                                                  'keyboard_instruments': keyboard_instruments,
                                                  'drums': drums,
                                                  'sound_system': sound_system,
                                                  'bestsellers': bestsellers,
                                                  'added_recently': added_recently,
                                                  'all_categories': all_categories}
                      )

    def post(self, request):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        all_categories = SubCategory.objects.all()
        bestsellers = Product.objects.filter(is_bestseller=True)[0:3]
        added_recently = Product.objects.filter(date_added__gte=date.today() - timedelta(days=3),
                                                date_added__lte=date.today())[0:3]
        key_word = request.POST.get('key_word')
        product_results = Product.objects.filter(name__icontains=key_word)
        category_results = Category.objects.filter(name__icontains=key_word)
        subcategory_results = SubCategory.objects.filter(name__icontains=key_word)
        return render(request, 'main/search_results.html', {'stringed_instruments': stringed_instruments,
                                                  'keyboard_instruments': keyboard_instruments,
                                                  'drums': drums,
                                                  'sound_system': sound_system,
                                                  'bestsellers': bestsellers,
                                                  'added_recently': added_recently,
                                                  'all_categories': all_categories,
                                                  'product_results': product_results,
                                                  'category_results': category_results,
                                                  'subcategory_results': subcategory_results}
                      )


class CategoryDetailsView(View):
    def get(self, request, category_id):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        subcategories = SubCategory.objects.filter(category_id=category_id)
        parent_category = CategorySubCategory.objects.filter(category_id=category_id)[0]
        return render(request, 'main/category_details.html', {'stringed_instruments': stringed_instruments,
                                                                'keyboard_instruments': keyboard_instruments,
                                                                'drums': drums,
                                                                'sound_system': sound_system,
                                                                'subcategories': subcategories,
                                                                'parent_category': parent_category}
                      )


class SubCategoryView(View):
    def get(self, request, subcategory_id):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        products = Product.objects.filter(subcategory_id=subcategory_id)
        parent_category = CategorySubCategory.objects.filter(subcategory_id=subcategory_id)[0]
        return render(request, 'main/subcategory_details.html', {'stringed_instruments': stringed_instruments,
                                                              'keyboard_instruments': keyboard_instruments,
                                                              'drums': drums,
                                                              'sound_system': sound_system,
                                                              'products': products,
                                                              'parent_category': parent_category})