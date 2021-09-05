# from django.shortcuts import render
from rest_framework import generics
from .serializers import CarsSerializer
from .models import Car
# Create your views here.

class CarsList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarsSerializer

class CarsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarsSerializer