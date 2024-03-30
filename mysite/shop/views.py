"""
The views module contains view functions for handling HTTP requests and rendering web pages.

This module includes view functions for various aspects of the web application, such as
displaying product listings.

Functions:
    index: Renders the index page of the shop application.
    product_detail: Renders the detail page for a specific product.
    process_order: Handles order processing.
    api_product_list: Returns a JSON response containing a list of products (API endpoint).
    api_product_detail: Returns a JSON response containing details of a specific product (API endpoint)
"""


from timeit import default_timer


from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiResponse
from .forms import ProductForm, GroupForm
from .models import Product, Order, ProductImage
from .serializers import ProductSerializer, OrderSerializer


# @extend_schema(description='Product CRUD')
class ProductViewSet(ModelViewSet):
    """
    A view set for interacting with the product resource.

    This view set provides CRUD (Create, Retrieve, Update, Delete) operations
    for the product resource. It supports listing all products, creating a new product,
    retrieving a specific product by ID, updating an existing product, and deleting a product.

    Attributes:
        queryset (QuerySet): The queryset representing all products in the database.
        serializer_class (Serializer): The serializer class used to serialize/deserialize
            product instances.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    search_fields = ["name", "description",]
    filterset_fields = [
        "name",
        "description",
        "price",
        "discount",
        "archived"
    ]
    ordering_fields = [
        "name",
        "price",
        "discount",
    ]

    @extend_schema(
        summary='Get one product by ID',
        description='Retrieves **product**, returns 404 if not found',
        responses={
            200: ProductSerializer,
            404: OpenApiResponse(description='Empty response, product by id not found'),
        }
    )
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)


class OrderViewSet(ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    search_fields = [
        "delivery_address", 'user'
    ]

    filterset_fields = [
        'delivery_address',
        'promocode',
        'user'
    ]

    ordering_fields = [
        'created_at',
        'user'
    ]
class ShopIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        products = [
            ('Laptop', 1999),
            ('Desktop', 2999),
            ('Smartphone', 999),
        ]
        context = {
            'time_running': default_timer(),
            'products': products,
            'items': 1,
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



class ProductDetailsView(DetailView):
    template_name = 'shop/products-details.html'
    model = Product
    context_object_name = "product"


class ProductsListView(ListView):
    template_name = 'shop/products.html'
    # model = Product
    queryset = Product.objects.filter(archived=False)
    context_object_name = 'products'


class ProductCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        # return self.request.user.groups.filter(name='secret-group').exists()
        return self.request.user.is_superuser

    model = Product
    fields = "name", "price", "description", "discount", "preview"
    # form_class = ProductForm
    success_url = reverse_lazy("shop:products")


class ProductUpdateView(UpdateView):
    model = Product
    # fields = "name", "description", "price", "discount", "preview"
    template_name_suffix = "_update_form"
    form_class = ProductForm

    def get_success_url(self):
        return reverse(
            "shop:product_details",
            kwargs={'pk': self.object.pk},
        )

    def form_valid(self, form):
        response = super().form_valid(form)
        for image in form.files.getlist("images"):
            ProductImage.objects.get_or_create(
                product=self.object,
                image=image,
            )

        return response
class ProductDeleteView(DeleteView):
    # model = Product
    queryset = Product.objects.prefetch_related("images")
    success_url = reverse_lazy('shop:products')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class OrdersListView(LoginRequiredMixin, ListView):
    queryset = (
        Order.objects
        .select_related('user')
        .prefetch_related('products')
    )


class OrderDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ["shop.view_order",]
    queryset = (
        Order.objects
        .select_related('user')
        .prefetch_related('products')
    )


class ProductsDataExportView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        products = Product.objects.order_by("pk").all()
        products_data = [
            {
                "pk": product.pk,
                "name": product.name,
                "price": product.price,
                "archived": product.archived,
            }
            for product in products
        ]
        return JsonResponse({"products": products_data})