from django.test import TestCase
from .models import Restaurant


class TestRestaurant(TestCase):
    def setUp(self):
        self.restaurant = Restaurant(name='Best Restaurant')
        self.restaurant.save()

    def tearDown(self):
        if Restaurant.objects.count() > 0:
            Restaurant.objects.all().delete()

    def test_str_returns_restaurant_name(self):
        entry = self.restaurant
        self.assertEqual(str(entry), entry.name)

    def test_add_restaurant_increases_count(self):
        new_restaurant = Restaurant(name='Worst Restaurant')
        new_restaurant.save()
        self.assertEqual(Restaurant.objects.count(), 2)
