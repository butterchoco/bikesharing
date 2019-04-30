from django import forms
from .models import Person

class tanggalWidget(forms.DateInput):
    input_type = 'date'


class signup_form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(signup_form, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Person
        fields = [
            'ktp',
            'nama',
            'email',
            'tgl_lahir',
            'no_telp',
            'alamat',
        ]
        widgets = {
            'tgl_lahir' : tanggalWidget(),
        }
