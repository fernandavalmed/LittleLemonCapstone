from django.test import TestCase
from Reservations.models import Menu


print("Test file is loaded")
class MenuTest(TestCase):

    def test_get_item(self):
        item = Menu.objects.create(Title="Ice Cream", Price=12, Inventory=5)
        self.assertEqual(f"{item.Title} : {item.Price}", "Ice Cream : 12")