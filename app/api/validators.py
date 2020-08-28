import requests
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def CarMakeValidator(make):

    url = (
        "https://vpic.nhtsa.dot.gov/api/vehicles/GetMakesForVehicleType/car?format=json"
    )

    r = requests.get(url)

    for carModel in r.json()["Results"]:
        if carModel["MakeName"].lower() == make.lower():
            return carModel["MakeName"]

    raise ValidationError(_("%(make)s is not a car make"), params={"make": make})


def CarModelValidator(make, model):

    url = (
        "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeyear/make/"
        + make
        + "/vehicleType/car?format=json"
    )

    r = requests.get(url)

    for carModel in r.json()["Results"]:
        if carModel["Model_Name"].lower() == model.lower():
            return carModel["Model_Name"]

    raise ValidationError(
        _("%(model)s is not a car model of %(make)s make"),
        params={"model": model, "make": make},
    )


def RateValidator(value):

    if value > 5:
        raise ValidationError(_("%(value)s is greater then 5"), params={"value": value})
    if value < 1:
        raise ValidationError(_("%(value)s is lower then 1"), params={"value": value})
