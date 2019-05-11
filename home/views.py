from django.shortcuts import render
from user.utils import ConnectDB
import requests

# Create your views here.


def index(request):
    if ('token' in request.session.keys()):
        headers = {'Authorization': 'Token ' + request.session['token']}
        dataPerson = requests.get(
            ConnectDB.BASE_URL + '/user/api/', headers=headers).json()
        dataTransaksi = requests.get(
            ConnectDB.BASE_URL + '/transaction/api/', headers=headers).json()
        if (len(dataTransaksi) != 0):
            dataPerson[0].update(dataTransaksi[0])
        response = dataPerson[0]
        return render(request, 'dashboard.html', response)
    else:
        return render(request, 'home.html')
