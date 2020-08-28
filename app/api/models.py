from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=128)
    model = models.CharField(max_length=128)

    def __str__(self):
        return "car(" + str(self.pk) + ") make:" + self.make + " model:" + self.model

    class Meta:
        unique_together = ("make", "model")


class CarRate(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rate = models.IntegerField()

    def __str__(self):
        return (
            "rate(" + str(self.pk) + f") got rate of {self.rate} for " + str(self.car)
        )
