from django import forms
from .models import CarType, Car, Review

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields='__all__'