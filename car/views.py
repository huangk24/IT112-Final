from django.shortcuts import render
from .models import Car, CarType, Review

# Create your views here.
def index(request):
    return render(request, 'car/index.html')

def cars(request):
    car_list = Car.objects.all()
    return render(request, 'car/cars.html', {'car_list': car_list})