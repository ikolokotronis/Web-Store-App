"""web_store_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import HomePageView, CategoryDetailsView, SubCategoryView, \
    ContactView, ShoppingCartView, ShoppingCartCheckoutView, \
    ShoppingCartRemoveProductView, ShoppingCartPaymentView, ShoppingCartSummaryView, \
    ShoppingCartSuccessView
from products.views import ProductView
from users.views import RegistrationView, LoginView, LogoutView, \
    UserPanelView, UserPanelEditView, PasswordResetView, UserPanelOrdersView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view()),
    path('contact/', ContactView.as_view()),
    path('product/<int:product_id>/', ProductView.as_view()),
    path('category/<int:category_id>/', CategoryDetailsView.as_view()),
    path('subcategory/<int:subcategory_id>/', SubCategoryView.as_view()),
    path('users/register/', RegistrationView.as_view()),
    path('users/login/', LoginView.as_view()),  #do zmiany na user
    path('users/logout/', LogoutView.as_view()), #do zmiany na user
    path('users/panel/<int:user_id>/', UserPanelView.as_view()), #do zmiany na user
    path('users/edit/<int:user_id>/', UserPanelEditView.as_view()),#do zmiany na user
    path('users/panel/orders/<int:user_id>/', UserPanelOrdersView.as_view()),
    path('users/password_reset/', PasswordResetView.as_view()), #do zmiany na user
    path('shopping_cart/<int:user_id>/', ShoppingCartView.as_view()),
    path('shopping_cart/<int:user_id>/checkout/', ShoppingCartCheckoutView.as_view()),
    path('shopping_cart/remove/<int:user_id>/<int:product_id>/', ShoppingCartRemoveProductView.as_view()),
    path('shopping_cart/<int:user_id>/<int:order_id>/payment/', ShoppingCartPaymentView.as_view()),
    path('shopping_cart/<int:user_id>/<int:order_id>/summary/', ShoppingCartSummaryView.as_view()),
    path('shopping_cart/<int:user_id>/<int:order_id>/success/', ShoppingCartSuccessView.as_view())
]
