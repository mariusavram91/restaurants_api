from django.test import TestCase
from django.test import Client
from .models import Restaurant


class TestRestaurant(TestCase):
    def setUp(self):
        self.client = Client()
        self.restaurant = Restaurant(name="Best Restaurant")
        self.restaurant.save()

    def tearDown(self):
        Restaurant.objects.all().delete()

    def test_root_returns_200(self):
        response = self.client.get('/')

        self.assertEquals(response.status_code, 200)

    def test_list_restaurants(self):
        new_restaurant = Restaurant(name='Worst Restaurant')
        new_restaurant.save()

        response = self.client.get('/restaurants/')

        self.assertEquals(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [
                {
                    'name': 'Best Restaurant',
                    'url': 'http://testserver/restaurants/Best%20Restaurant/'
                },
                {
                    'name': 'Worst Restaurant',
                    'url': 'http://testserver/restaurants/Worst%20Restaurant/'
                }
            ]
        )

    def test_post_new_restaurant(self):
        params = {'name': 'Worst Restaurant'}
        response = self.client.post('/restaurants/', params, format='json')

        self.assertEquals(response.status_code, 201)
        self.assertEqual(Restaurant.objects.count(), 2)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {
                'name': 'Worst Restaurant',
                'url': 'http://testserver/restaurants/Worst%20Restaurant/'
            }
        )

    def test_delete_restaurant(self):
        response = self.client.delete('/restaurants/Best%20Restaurant/')

        self.assertEquals(response.status_code, 204)

    def test_random_restaurant(self):
        response = self.client.get('/restaurants/random/')

        self.assertEquals(response.status_code, 200)
