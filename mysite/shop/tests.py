from random import choices
from string import ascii_letters

from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from shop.models import Product
from shop.utils import add_two_numbers

class AddTwoNumbersTestCase(TestCase):
    def test_add_two_numbers(self):
        result = add_two_numbers(2, 3)
        self.assertEqual(result, 5)


class ProductCreateViewTestCase(TestCase):

    def setUp(self) -> None:
        self.product_name = "".join(choices(ascii_letters, k=10))
        Product.objects.filter(name=self.product_name).delete()
    def test_create_product(self):
        response = self.client.post(
            reverse("shop:create_product"),
            {
                "name": self.product_name,
                "price": "123.45",
                "description": "A good table",
                "discount": "10"
            }
        )

        self.assertRedirects(response, '/myauth/login/?next=/shop/products/create/')
        self.assertTrue(
            Product.objects.filter(name=self.product_name).exists()
        )


class ProductDetailsViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.product = Product.objects.create(name="Best Product")

    @classmethod
    def tearDownClass(cls):
        cls.product.delete()

    def test_get_product(self):
        response = self.client.get(
            reverse("shop:product_details", kwargs={"pk": self.product.pk})
        )

        self.assertEqual(response.status_code, 200)

    def test_get_product_and_check_content(self):
        response = self.client.get(
            reverse("shop:product_details", kwargs={"pk": self.product.pk})
        )

        self.assertContains(response, self.product.name)


class ProductListViewTestCase(TestCase):
    fixtures = [
        'products-fixtures.json',
    ]

    def test_products(self):
        response = self.client.get(reverse("shop:products"))

        # for product in Product.objects.filter(archived=False).all():
        #     self.assertContains(response, product.name)

        # products = Product.objects.filter(archived=False).all()
        # products_ = response.context["products"]
        # for p, p_ in zip(products, products_):
        #     self.assertEqual(p.pk, p_.pk)

        self.assertQuerysetEqual()(
            qs=Product.objects.filter(archived=False).all(),
            values=[p.pk for p in response.context["products"]],
            transform=lambda p: p.pk,
        )

        self.assertTemplateUsed(response, 'shop/products.html')


class OrdersListViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.credentials = dict(username='Bob_test', password='qwerty')
        # cls.user = User.objects.create_user(**cls.credentials)

        cls.user = User.objects.create_user(username='Bob_test', password='qwerty')
    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
    def setUp(self) -> None:

        # self.client.login(**self.credentials)

        self.client.force_login(self.user)
    def test_orders_view(self):
        response = self.client.get(reverse("shop:orders"))
        self.assertContains(response, "Orders")


    def test_orders_view_not_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse("shop:orders"))

        # self.assertRedirects(response, str(settings.LOGIN_URL))

        self.assertEqual(response.status_code, 302)
        self.assertIn(str(settings.LOGIN_URL), response.url)





# TDD - Test-Driven Development
class ProductExportViewTestCase(TestCase):
    fixtures = [
        'product-fixtures.json',
    ]

    def test_get_products_view(self):
        response = self.client.get(
            reverse("shop:products-export"),
        )
        self.assertEqual(response.status_code, 200)
        products = Product.objects.order_by("pk").all()
        expected_data = [
            {
                "pk": product.pk,
                "name": product.name,
                "price": str(product.price),
                "archived": product.archived,
            }
            for product in products
        ]

        products_data = response.json()
        self.assertEqual(
            products_data["products"],
            expected_data
        )