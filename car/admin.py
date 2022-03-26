from django.contrib import admin
from .models import CarType, Car, Review

# Register your models here.
admin.site.register(CarType)
admin.site.register(Car)
admin.site.register(Review)