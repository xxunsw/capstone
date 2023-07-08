from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        MenuItem.objects.create(title="Pizza", price=10.99, inventory=50)
        MenuItem.objects.create(title="Burger", price=8.99, inventory=30)
        MenuItem.objects.create(title="Salad", price=5.99, inventory=20)

    def test_getall(self):
        response = self.client.get('/api/menu/')
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

