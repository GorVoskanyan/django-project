from django.core.management import BaseCommand
from shop.models import Product


class Command(BaseCommand):
    '''
    Create products
    '''

    def handle(self, *args, **options):
        self.stdout.write('Create Products')

        products = [
            'Laptop',
            'Desktop',
            'Smartphone',
        ]

        prices = [
            2999,
            1999,
            999
        ]

        for product, price in zip(products, prices):
            name, created = Product.objects.get_or_create(name=product, price=price)
            self.stdout.write(f'Create product {product} for {price}')

        self.stdout.write(self.style.SUCCESS('Products created'))