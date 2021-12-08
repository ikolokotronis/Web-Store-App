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
from main.views import HomePageView, CategoryDetailsView, KeyboardsSubCategoryView
from products.views import ProductView
from users.views import RegistrationView, LoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view()),
    path('product/<int:product_id>/', ProductView.as_view()),
    path('category/<int:category_id>/', CategoryDetailsView.as_view()),
    path('category/<int:category_id>/<int:subcategory_id>/', KeyboardsSubCategoryView.as_view()),
    path('users/register/', RegistrationView.as_view()),
    path('users/login/', LoginView.as_view())
]
