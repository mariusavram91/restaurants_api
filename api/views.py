import random
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantsView(viewsets.ModelViewSet):
    """
    A ViewSet for listing, creating, and deleting restaurants.

    ModelViewSet includes already actions like list(), create(), and delete().

    retrieve:
    Return the restaurant.

    list:
    Return a list of all the existing restaurants.
    Optional query param: /?sort=true

    create:
    Create a new restaurants.

    retrieve:
    Delete the restaurant.

    random:
    Return a random restaurant.
    """

    serializer_class = RestaurantSerializer
    lookup_field = 'name'

    def get_queryset(self):
        """
        Optionally sorts by the name of the restaurants when the 'sort' query
        parameter is 'true' in the URL.
        """

        queryset = Restaurant.objects.all()
        sort = self.request.query_params.get('sort')

        if sort and sort == 'true':
            queryset = queryset.order_by('name')

        return queryset

    @action(detail=False)
    def random(self, request):
        restaurants_ids = Restaurant.objects.values_list('pk', flat=True)
        random_restaurant_id = random.choice(list(restaurants_ids))
        random_restaurant = Restaurant.objects.get(id=random_restaurant_id)
        serializer = self.get_serializer(random_restaurant, many=False)

        return Response(serializer.data)
