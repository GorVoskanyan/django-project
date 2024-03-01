from django.urls import path
from .views import (
    ShopIndexView,
    GroupsListView,
    ProductDetailsView,
    ProductsListView,
    orders_list,
    create_product
)

app_name = 'shop'

urlpatterns = [
    path('', ShopIndexView.as_view(), name='index'),
    path('groups/', GroupsListView.as_view(), name='groups'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailsView.as_view(), name='product_details'),
    path('products/create/', create_product, name='create_product'),
    path('orders/', orders_list, name='orders'),
]