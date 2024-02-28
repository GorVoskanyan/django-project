from timeit import default_timer


from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import Group

from .forms import ProductForm
from .models import Product, Order


# Create your views here.

def shop_index(request: HttpRequest):
    # print(request.path)
    # print(request.method)
    # print(request.headers)

    # return HttpResponse('Hello World!')
    products = [
        ('Laptop', 1999),
        ('Desktop', 2999),
        ('Smartphone', 999),
    ]
    context = {
        'time_running': default_timer(),
        'products': products
    }
    return render(request, 'shop/index.html', context=context)


def groups_list(request: HttpRequest):
    context = {
        'groups': Group.objects.all()
    }
    return render(request, 'shop/groups.html', context=context)

def product_list(request: HttpRequest):
    context = {
        'products': Product.objects.all()
    }

    return render(request, 'shop/products.html', context=context)


def create_product(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data('name')
            # Product.objects.create(**form.cleaned_data)
            form.save()
            url = reverse('shop:products')
            return redirect(url)
    else:
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'shop/create-product.html', context=context)

def orders_list(request: HttpRequest):
    context = {
        'orders': Order.objects.select_related('user').prefetch_related('products').all(),
    }

    return render(request, 'shop/orders.html', context=context)