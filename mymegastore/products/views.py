from django.shortcuts import render
from .models import ProductCategory, Product

def index(request):
    context = {
        'title' : 'myramasa666'
    }
    return render(request, 'index.html', context = context)


def products(request):
    context = {
        'title' : 'Каталог',
        'products' : Product.objects.all(),
        'categories' : ProductCategory.objects.all(),
    }
    return render(request, 'products.html', context = context)
