from django.shortcuts import render, redirect
from django.views import View
from main.models import Category, ShoppingCart, SubCategory
from products.models import Product, SubCategoryProduct
from users.models import WebsiteUser

all_categories = Category.objects.all()
all_subcategories = SubCategory.objects.all().order_by('name')


class ProductView(View):
    def get(self, request, product_id):
        """
        Displays information about a specific product, with the option to add it to the shopping cart
        :param request:
        :param product_id:
        :return product details page:
        """
        shopping_cart_list = ShoppingCart.objects.filter(user_id=request.user.id)
        product = Product.objects.get(id=product_id)
        subcategory = SubCategoryProduct.objects.filter(product_id=product_id)[0]
        last_viewed_products = ""
        cleared_last_viewed_products = []
        displayed_last_viewed_products = []
        if request.session.get('last_viewed_products'):
            last_viewed_products = request.session.get('last_viewed_products').split(',')
            request.session['last_viewed_products'] += f'{product.id},'
            for product_id in last_viewed_products:
                if product_id:
                    if product_id in displayed_last_viewed_products:
                        pass
                    else:
                        displayed_last_viewed_products.append(product_id)
                        cleared_last_viewed_products.append(Product.objects.get(id=product_id))

        else:
            request.session['last_viewed_products'] = f'{product.id},'

        return render(request, 'product/product_details.html', {'all_categories': all_categories,
                                                                'all_subcategories': all_subcategories,
                                                                'product': product,
                                                                'shopping_cart_list': shopping_cart_list,
                                                                'subcategory': subcategory,
                                                                'cleared_last_viewed_products': cleared_last_viewed_products[::-1][0:6]
                                                                }
                      )

    def post(self, request, product_id):
        quantity = request.POST.get('quantity')
        product = Product.objects.get(id=product_id)
        user = WebsiteUser.objects.get(id=request.user.id)
        ShoppingCart.objects.create(product=product, user=user, quantity=quantity)
        return redirect(f'/product/{product.id}/')
