from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shop.models import Product

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Start demo selecting fields...')

        users_info = User.objects.values_list('username', flat=True)
        print(list(users_info))
        for user_info in users_info:
            print(user_info)

        # products_values = Product.objects.values('pk', 'name')
        # for p_value in products_values:
        #     print(p_value)

        self.stdout.write(self.style.SUCCESS('Done!'))