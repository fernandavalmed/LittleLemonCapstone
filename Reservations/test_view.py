from django.test import TestCase
from Reservations.models import Menu

class MenuViewTest(TestCase):

    def setUp(self):
        item = Menu.objects.create(Title="Tacos", Price=7, Inventory=20)
        print(item)

    def test_getall(self):
        items = Menu.objects.all()
        self.assertEqual(str(items[0]), "Tacos : 7.00")