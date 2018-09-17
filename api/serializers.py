from rest_framework import serializers
from .models import Restaurant


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='restaurants-detail',
        lookup_field='name'
    )

    class Meta:
        model = Restaurant
        fields = ('url', 'name',)
