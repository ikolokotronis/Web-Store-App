from django.shortcuts import render
from django.views import View
from main.models import Category, ShoppingCart, SubCategory
from products.models import Product, SubCategoryProduct
from users.models import WebsiteUser
from django.http import HttpResponse


class ProductView(View):
    def get(self, request, product_id):
        """
        Displays information about a specific product, with the option to add it to the shopping cart
        :param request:
        :param product_id:
        :return product details page:
        """
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        product = Product.objects.get(id=product_id)
        shopping_cart = ShoppingCart.objects.all()
        subcategory = SubCategoryProduct.objects.filter(product_id=product_id)[0]
        last_viewed_products = []
        response = render(request, 'product/product_details.html', {'product': product,
                                                                'shopping_cart_list': shopping_cart,
                                                                'subcategory': subcategory,
                                                                'last_viewed_products': last_viewed_products,
                                                                    'all_categories': all_categories,
                                                                    'all_subcategories': all_subcategories,
                                                                    }
                      )
        if request.COOKIES.get('last_viewed_product'):
            last_viewed_products.append(request.COOKIES.get('last_viewed_product'))
        else:
            response.set_cookie(key='last_viewed_product', value=product, max_age=3600)
            last_viewed_products.append(request.COOKIES.get('last_viewed_product'))
            return response
        return render(request, 'product/product_details.html', {'all_categories': all_categories,
                                                                'all_subcategories': all_subcategories,
                                                  'product': product,
                                                                'shopping_cart_list': shopping_cart,
                                                                'subcategory': subcategory,
                                                                'last_viewed_products': last_viewed_products}
                      )

    def post(self, request, product_id):
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        quantity = request.POST.get('quantity')
        product = Product.objects.get(id=product_id)
        user = WebsiteUser.objects.get(id=request.user.id)
        shopping_cart = ShoppingCart.objects.all()
        ShoppingCart.objects.create(product=product, user=user, quantity=quantity)
        return render(request, 'product/product_details.html', {'all_categories': all_categories,
                                                                'all_subcategories': all_subcategories,
                                                                'product': product,
                                                                'success_text': 'Product added to cart',
                                                                'shopping_cart_list': shopping_cart}
                      )