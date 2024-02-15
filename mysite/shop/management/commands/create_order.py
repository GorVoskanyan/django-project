from django.core.management import BaseCommand
from django.contrib.auth.models import User

from shop.models import Order

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Create order')
        user = User.objects.get(username='admin')

        order, created = Order.objects.get_or_create(
            delivery_address='Avenue Komitas 15',
            promocode='promo888',
            user=user,

        )

        self.stdout.write(f'Created order {order}')