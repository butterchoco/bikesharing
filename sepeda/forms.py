from django import forms
from .models import Sepeda_models

daftar_status = (
    ('1', 'tersedia'),
    ('2', 'tidak tersedia'),
)

class sepeda_forms(forms.Form):
    attrs = {
        'class': 'form-control'
    }

    merk = forms.CharField(label = "Brand", max_length= 10, required=True, widget = forms.TextInput(attrs = attrs))
    jenis = forms.CharField(label = "Type", max_length=50, required=True, widget = forms.TextInput(attrs = attrs))
    status = forms.ChoiceField(label = "Status", choices=daftar_status)
    stasiun = forms.CharField(label = "Station ID", max_length = 10, required=True, widget = forms.PasswordInput(attrs = attrs))
    penyumbang = forms.CharField(label = "Number of Donor", required = True, max_length=20, widget = forms.TextInput(attrs = attrs))