from typing import Sequence

from django.core.management import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction

from shop.models import Order, Product

class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write('Create order with products.')
        user = User.objects.get(username='admin')
        products: Sequence[Product] = Product.objects.all()
        order, created = Order.objects.get_or_create(
            delivery_address='Avenue Arshakunyats 15',
            promocode='promo888',
            user=user,
        )

        for product in products:
            order.products.add(product)
        order.save()
        order + 1
        self.stdout.write(f'Created order {order}')