"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views
from mysite import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('shopcart',views.shop_cart_list, name='shopcart'),
    path('addtocart/<int:proid>',views.shop_cart_add, name='addtocart'),
    path('deletefromcart/<int:id>',views.shop_cart_delete, name='deletefromcart'),
    path('checkout',views.shop_cart_checkout,name='checkout'),
    path('detail/<int:id>',views.order_detail,name='orderdetail'),
    path('profil',views.profil,name='profil'),

]
