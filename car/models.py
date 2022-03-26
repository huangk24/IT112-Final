from django.db import models
from  django.contrib.auth.models import User

# Create your models here.

class CarType(models.Model):
    typename = models.CharField(max_length = 255)
    typedescription = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.typename

    class Meta:
        db_table = 'cartype'

class Car(models.Model):
    carname = models.CharField(max_length = 255)
    cartype = models.ForeignKey(CarType, on_delete = models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    dateentered = models.DateField()
    price = models.DecimalField(max_digits = 9, decimal_places = 2)
    producturl = models.URLField()

    def __str__(self):
        return self.carname

    class Meta:
        db_table = 'car'

class Review(models.Model):
    title = models.CharField(max_length = 255)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    car = models.ForeignKey(Car, on_delete = models.CASCADE)
    reviewdate = models.DateField()
    reviewtext = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'review'