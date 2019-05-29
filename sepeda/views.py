from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from user.utils import ConnectDB
from datetime import datetime
import requests
import random

# Create your views here.
def sepeda_regist(request):
	return render(request, 'sepeda.html')

# def sepeda_lists(request):
#     return render(request, 'sepeda_lists.html')

class SepedaAPI(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        user = request.user
        data = ConnectDB.getAllDataWithQuery(
                '''
                SELECT * FROM sepeda
                '''
            )
        return Response(data)


def sepeda_lists(request):
    person = ConnectDB.getUserDataWithApi(request)
    response = ConnectDB.getPersonalDataWithApi(request, 'sepeda', '/sepeda/api/')
    print(response)
    response.update(person)
    return render(request, 'sepeda.html', response)

def add_sepeda(request):
    if (request.method == "POST"):
        nomor = random.randint(0, 100000)
        merk = request.POST.get('brand', None)
        jenis = request.POST.get('type', None)
        status = request.POST.get('status', None)
        stasiun = request.POST.get('station', None)
        penyumbang = request.POST.get('pendonor', None)
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO sepeda VALUES(%s, %s, %s, %s, %s, %s)", [
                nomor, merk, jenis, status, stasiun, penyumbang])
        return HttpResponse("SUCCESS 200")
    else:
        return HttpResponse("HTTP 204")

def delete_sepeda(request):
    if (request.method == "POST"):
        nomor = request.POST.get('number', None)
        with connection.cursor() as cursor:
            cursor.execute("DELETE from sepeda WHERE nomor=%s", [nomor])
        return HttpResponse("SUCCESS 200")
    else:
        return HttpResponse("HTTP 204")

def update_sepeda(request):
    if (request.method == "POST"):
        nomor = request.POST.get('number', None)
        merk = request.POST.get('brand', None)
        jenis = request.POST.get('type', None)
        status = request.POST.get('status', None)
        stasiun = request.POST.get('station', None)
        penyumbang = request.POST.get('pendonor', None)
        with connection.cursor() as cursor:
            cursor.execute('''
            UPDATE sepeda 
            SET merk=%s, jenis=%s, status=%s, id_stasiun=%s, no_kartu_penyumbang=%s
            WHERE nomor=%s
            ''', [merk, jenis, status, stasiun, penyumbang, nomor])
        return HttpResponse("SUCCESS 200")
    else:
        return HttpResponse("HTTP 204")