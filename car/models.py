from django.db import models


class CarType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Car(models.Model):
    car = models.ForeignKey(CarType, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    country = models.CharField(max_length=60)
    price = models.IntegerField()

    def __str__(self):
        return str(self.model)
