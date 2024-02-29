from django.urls import path
from .views import (
    ShopIndexView,
   GroupsListView,
    product_list,
    orders_list,
    create_product
)

app_name = 'shop'

urlpatterns = [
    path('', ShopIndexView.as_view(), name='index'),
    path('groups/', GroupsListView.as_view(), name='groups'),
    path('products/', product_list, name='products'),
    path('products/create/', create_product, name='create_product'),
    path('orders/', orders_list, name='orders'),
]