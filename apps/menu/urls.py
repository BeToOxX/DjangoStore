from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('menu/', menu, name='menu'),
    path('services/', services, name='services'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
    path('room/', room, name='room'),
    path('shop/', shop, name='shop'),
    path('product-single/', productsingle, name='productsingle'),
    path('checkout/', checkout, name='checkout'),
    path('cart/', cart, name='cart'),
    path('blog-single/', blogsingle, name='blogsingle'),
]
