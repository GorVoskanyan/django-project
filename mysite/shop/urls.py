from django.urls import path
from .views import shop_index, groups_list, product_list, orders_list, create_product

app_name = 'shop'

urlpatterns = [
    path('', shop_index, name='index'),
    path('groups/', groups_list, name='groups'),
    path('products/', product_list, name='products'),
    path('products/create/', create_product, name='create_product'),
    path('orders/', orders_list, name='orders'),

]