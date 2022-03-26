from django.shortcuts import render, get_object_or_404
from .models import Car, CarType, Review
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'car/index.html')

def cars(request):
    car_list = Car.objects.all()
    return render(request, 'car/cars.html', {'car_list': car_list})

def carDetail(request, id):
    car = get_object_or_404(Car, pk = id)
    return render(request, 'car/cardetail.html', {'car': car})