from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import CarType, Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
