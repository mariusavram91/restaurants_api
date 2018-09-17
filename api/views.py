import random
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantsView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = 'name'

    @action(detail=False)
    def random(self, request):
        restaurants_ids = Restaurant.objects.values_list('pk', flat=True) \
            .order_by('pk')
        random_restaurant_id = random.choice(list(restaurants_ids))
        random_restaurant = Restaurant.objects.get(id=random_restaurant_id)
        serializer = self.get_serializer(random_restaurant, many=False)

        return Response(serializer.data)
