from django import forms
from .models import Stasiun_models

class stasiun_forms(forms.Form):
    attrs = {
        'class': 'form-control'
    }

    nama = forms.CharField(label = "Nama", max_length= 10, required=True, widget = forms.TextInput(attrs = attrs))
    alamat = forms.CharField(label = "Alamat", max_length=50, required=True, widget = forms.TextInput(attrs = attrs))
    latitude = forms.CharField(label = "Latitude", max_length = 50, required=True, widget = forms.TextInput(attrs = attrs))
    longitude = forms.CharField(label = "Longitude", max_length = 50, required=True, widget = forms.TextInput(attrs = attrs))
