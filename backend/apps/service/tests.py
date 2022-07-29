from django.test import TestCase
from django.urls import reverse
from factory.django import DjangoModelFactory
# Create your tests here.
from backend.apps.service.models import  Product


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product
    name = "Product Name"
    description = "Product Description"
    price = 1450.00
    quantity = 10


class ProductQuantityEditTest(TestCase):

    def setUp(self):
        self.product = ProductFactory()

    def post(self, url, data):
        return self.client.post(url, data=data)

    def test_add_product_quantity(self):
        url = reverse("quantity_update", kwargs={"pk":self.product.pk})
        data = {
            "quantity": 10
        }
        response = self.post(url, data)
        object = Product.objects.get(pk=self.product.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(object.quantity, 20)

    def test_update_product_quantity(self):
        url = reverse("quantity_update", kwargs={"pk": self.product.pk})
        data = {
            "quantity": 100
        }
        url += "?q=update"
        response = self.post(url, data)
        object = Product.objects.get(pk=self.product.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(object.quantity, 100)
