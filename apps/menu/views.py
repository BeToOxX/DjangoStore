from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    allproduct = product.objects.filter(fk_tipo_producto=1)
    alldrinks = product.objects.filter(fk_tipo_producto=2)
    allpostres = product.objects.filter(fk_tipo_producto=3)
    return render(request, 'index.html', {'allproduct':allproduct,'alldrinks':alldrinks})

def contact(request):
    return render(request, 'contact.html')

def menu(request):
    return render(request, 'menu.html')

def services(request):
    return render(request, 'services.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def room(request):
    return render(request, 'room.html')

def shop(request):
    return render(request, 'shop.html')

def productsingle(request):
    return render(request, 'product-single.html')

def checkout(request):
    return render(request, 'checkout.html')

def cart(request):
    return render(request, 'cart.html')

def blogsingle(request):
    return render(request, 'blog-single.html')

#def detalle(request):
#    return render(request, 'detalle/menu.html')