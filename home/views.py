from django.shortcuts import render
from user.utils import ConnectDB
import requests

# Create your views here.


def index(request):
    response = {}
    if ('token' in request.session.keys()):
        headers = {'Authorization': 'Token ' + request.session['token']}
        dataTransaksi = requests.get(
            ConnectDB.BASE_URL + '/transaction/api/', headers=headers).json()
        dataLaporan = requests.get(
            ConnectDB.BASE_URL + '/report/api/', headers=headers).json()
        dataPerson = requests.get(
            ConnectDB.BASE_URL + '/user/api/', headers=headers).json()
        response.update(dataPerson[0])
        if (len(dataTransaksi) != 0):
            response.update(dataTransaksi[0])
        if (len(dataLaporan) != 0):
            response.update(dataLaporan[0])
        return render(request, 'dashboard.html', response)
    else:
        return render(request, 'home.html')
