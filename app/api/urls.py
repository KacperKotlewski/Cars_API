from django.urls import include, path
from rest_framework import routers

from .viewsets import CarRateViewSet, PopularCarsViewSet
from .views import api_overview, cars

router = routers.DefaultRouter()
router.register("rate", CarRateViewSet, basename="rate")
router.register("popular", PopularCarsViewSet, basename="popular")

app_name = "api"

urlpatterns = [
    path("", api_overview, name="api_overview"),
    path("cars/", cars, name="cars"),
    path("", include(router.urls)),
]
