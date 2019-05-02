from django.shortcuts import render
from User.forms import signup_form

# Create your views here.


def index(request):
    form = signup_form()
    return render(request, 'home.html', {'form': form})
