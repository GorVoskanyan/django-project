from django.core.management import BaseCommand

from shop.models import Product

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Start demo Bulk actions')

        result = Product.objects.filter(
            name__contains='Smartphone'
        ).update(discount=10)
        print(result)

        # info = [
        #     ('Smartphone 1', 1999),
        #     ('Smartphone 2', 2999),
        #     ('Smartphone 3', 3999),
        # ]
        #
        # products = [
        #     Product(name=name, price=price)
        #     for name, price in info
        # ]
        #
        # result = Product.objects.bulk_create(products)
        # for obj in result:
        #     print(obj)

        self.stdout.write('End demo Bulk actions')