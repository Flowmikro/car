from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .models import CarType, Car
from .serializers import CarSerializer


# class CarAPIView(generics.ListCreateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#
#
# class CarAPIViewPut(generics.UpdateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#

class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
