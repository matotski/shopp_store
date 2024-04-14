from django.shortcuts import render, HttpResponseRedirect
from .models import ProductCategory, Product, Basket
from django.urls import reverse

from django.contrib.auth.decorators import login_required



def index(request):
    context = {
        'title' : 'myramasa666'
    }
    return render(request, 'index.html', context = context)


def products(request, category_id=None):
    if category_id:
        category = ProductCategory.objects.get(id = category_id)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    context = {
        'title' : 'Каталог',
        'products' : products,
        'categories' : ProductCategory.objects.all(),
    }
    return render(request, 'products.html', context = context)

@login_required
def basket_add(request, product_id:id):
    product = Product.objects.get(id = product_id)
    baskets = Basket.objects.filter(user = request.user, product = product)

    if not baskets.exists():
        Basket.objects.create(user = request.user, product = product, quantity = 1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(reverse('products:index'))
@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id = basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])