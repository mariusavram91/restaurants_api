from django.urls import include, path
from rest_framework import routers
from .views import RestaurantsView

router = routers.DefaultRouter()

router.register(r"restaurants", RestaurantsView, base_name='restaurants')

urlpatterns = [
    path('', include(router.urls)),
]
