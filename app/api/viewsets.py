from rest_framework import mixins, viewsets

from .models import Car, CarRate
from .utils import Cars_List, Popular_Cars_List
from .serializers import CarRateSerializer, CarSerializer


class CarRateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = CarRate.objects.all()
    serializer_class = CarRateSerializer


class PopularCarsViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = CarRate.objects.all()
    serializer_class = CarSerializer

    def list(self, request, *args, **kwargs):
        return Popular_Cars_List()


class CarViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def list(self, request, *args, **kwargs):
        return Cars_List()
