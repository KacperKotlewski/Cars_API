from django.test import Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Car, CarRate
from .serializers import CarWithRateSerializer

client = Client()


class CarsTest(APITestCase):
    def setUp(self):
        Car.objects.create(make="JAGUAR", model="Vanden Plas")
        Car.objects.create(make="ford", model="mustang")
        Car.objects.create(make="TESLA", model="s")
        Car.objects.create(make="BMW", model="X1")
        Car.objects.create(make="NISSAN", model="200SX")

        self.base_cars_count = Car.objects.count()
        self.url = reverse("api:cars")
        self.test_car_data = {"make": "FERRARI", "model": "Testarossa"}

    def test_get_all_cars(self):

        response = client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.base_cars_count)

    def test_append_car(self):

        response = client.post(self.url, self.test_car_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Car.objects.count(), self.base_cars_count + 1)

    def test_dont_duplicate_car(self):

        response = client.post(self.url, self.test_car_data)

        expected_count = self.base_cars_count + 1

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Car.objects.count(), expected_count)

        response = client.post(self.url, self.test_car_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Car.objects.count(), expected_count)


class CarRateTest(APITestCase):
    def setUp(self):
        cars = [
            Car.objects.create(make="JAGUAR", model="Vanden Plas"),
            Car.objects.create(make="ford", model="mustang"),
            Car.objects.create(make="TESLA", model="s"),
        ]

        CarRate.objects.create(car=cars[1], rate=5)
        CarRate.objects.create(car=cars[2], rate=4)
        CarRate.objects.create(car=cars[2], rate=5)

        self.base_CarRate_count = CarRate.objects.count()

    def test_append_rate(self):

        rate_url = reverse("api:rate-list")
        data = {"car": 3, "rate": 5}
        response = client.post(rate_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CarRate.objects.count(), self.base_CarRate_count + 1)

    def test_check_rates(self):

        cars_url = reverse("api:cars")
        response = client.get(cars_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = CarWithRateSerializer(response.data, many=True)

        # based on values that we setup before we should get rates for:
        # - Vanden Plas = null //None
        # - mustang = 5.0
        # - tesla s = 4.5
        self.assertEqual(serializer.data[0]["rate"], None)
        self.assertEqual(serializer.data[1]["rate"], "5.0")
        self.assertEqual(serializer.data[2]["rate"], "4.5")

    def test_most_popular(self):

        popular_url = reverse("api:popular-list")
        response = client.get(popular_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        popular_data = response.data

        # based on values that we setup before we should have sorted popular response data as exacly reversed cars response data
        cars_url = reverse("api:cars")
        cars_data = client.get(cars_url).data[::-1]  # getting cars and reverse data
        self.assertEqual(popular_data[0]["id"], cars_data[0]["id"])
        self.assertEqual(popular_data[1]["id"], cars_data[1]["id"])
        self.assertEqual(popular_data[2]["id"], cars_data[2]["id"])
