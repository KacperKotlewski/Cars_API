import statistics

from rest_framework.response import Response

from .models import Car, CarRate
from .serializers import CarRateSerializer, CarSerializer, CarWithRateSerializer


# function to list all cars
def Cars_List():
    serializer = CarWithRateSerializer(Get_Cars_Dict(sum_rates=True), many=True)
    return Response(serializer.data)


# function to list all cars by popularity
def Popular_Cars_List():
    sort_cars = sorted(
        Get_Cars_Dict(count_rates=True), key=lambda k: k["count_of_rates"], reverse=True
    )

    serializer = CarSerializer(sort_cars, many=True)
    return Response(serializer.data)


# function to generate custom cars dict based on Car model data
def Get_Cars_Dict(sum_rates=False, count_rates=False):
    cars_queryset = Car.objects.all()
    cars_dict = []

    for car in cars_queryset:
        new_car = {"id": car.id, "make": car.make, "model": car.model}

        if sum_rates:
            new_car["rate"] = Get_Average_Rate(car)

        if count_rates:
            new_car["count_of_rates"] = CarRate.objects.filter(car=car).count()

        cars_dict.append(new_car)

    return cars_dict


# function for geting average rate for single car object
def Get_Average_Rate(car):
    try:
        return statistics.mean([r.rate for r in CarRate.objects.filter(car=car)])
    except statistics.StatisticsError:
        pass
    return None
