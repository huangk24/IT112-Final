from django.shortcuts import render, get_object_or_404
from .models import Car, CarType, Review
from django.urls import reverse_lazy
from .forms import CarForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'car/index.html')

def cars(request):
    car_list = Car.objects.all()
    return render(request, 'car/cars.html', {'car_list': car_list})

def carDetail(request, id):
    car = get_object_or_404(Car, pk = id)
    return render(request, 'car/cardetail.html', {'car': car})

@login_required
def newCar(request):
    form = CarForm

    if request.method == 'POST':
        form=CarForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = CarForm()
    else:
        form = CarForm()
    return render(request, 'car/newcar.html', {'form': form})

def loginmessage(request):
    return render(request, 'car/loginmessage.html')

def logoutmessage(request):
    return render(request, 'car/logoutmessage.html')