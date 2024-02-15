from django.core.management import BaseCommand

from shop.models import Order, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        order = Order.objects.first()
        if not order:
            self.stdout.write(('no order found'))
            return

        products = Product.objects.all()
        for product in products:
            order.products.add(product)

        order.save()

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully adde products {order.products.all()} to order {order}'
            )
        )

