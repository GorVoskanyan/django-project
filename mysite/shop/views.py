from timeit import default_timer


from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from .forms import ProductForm, GroupForm
from .models import Product, Order


class ShopIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
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


class GroupsListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "form": GroupForm(),
            'groups': Group.objects.all()
        }
        return render(request, 'shop/groups.html', context=context)

    def post(self, request: HttpRequest):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect(request.path)


# class ProductDetailsView(View):
#     def get(self, request: HttpRequest, pk: int) -> HttpResponse:
#         product = get_object_or_404(Product, pk=pk)
#         context = {
#             'product': product,
#         }
#         return render(request, "shop/products-details.html", context=context)


class ProductDetailsView(DetailView):
    template_name = 'shop/products-details.html'
    model = Product
    context_object_name = "product"


# class ProductsListView(TemplateView):
#     template_name = 'shop/products.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["products"] = Product.objects.all()
#         return context

class ProductsListView(ListView):
    template_name = 'shop/products.html'
    model = Product
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    fields = "name", "price", "description", "discount"
    # form_class = ProductForm
    success_url = reverse_lazy("shop:products")


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


class OrdersListView(ListView):
    queryset = (
        Order.objects
        .select_related('user')
        .prefetch_related('products')
    )


class OrderDetailView(DetailView):
    queryset = (
        Order.objects
        .select_related('user')
        .prefetch_related('products')
    )