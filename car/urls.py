from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('cars/', views.cars, name = 'cars'),
    path('carDetail/<int:id>', views.carDetail, name = 'detail'),
    path('newcar/', views.newCar, name = 'newcar'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]