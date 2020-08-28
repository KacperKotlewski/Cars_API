from rest_framework import serializers

from .models import Car, CarRate
from .validators import CarMakeValidator, CarModelValidator, RateValidator


class CarSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        attrs["make"] = CarMakeValidator(attrs["make"])
        attrs["model"] = CarModelValidator(attrs["make"], attrs["model"])
        return super().validate(attrs)

    class Meta:
        model = Car
        fields = "__all__"


class CarRateSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        RateValidator(attrs["rate"])
        return super().validate(attrs)

    class Meta:
        model = CarRate
        fields = "__all__"
        extra_kwargs = {"rate": {"min_value": 1, "max_value": 5}}


class CarWithRateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    make = serializers.CharField(max_length=128)
    model = serializers.CharField(max_length=128)
    rate = serializers.DecimalField(
        decimal_places=1, max_digits=5, allow_null=True, default=None
    )
