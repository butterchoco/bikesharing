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
def stasiun_regis(request):
	return render(request, 'stasiun.html')

# def stasiun_lists(request):
# 	return render(request, 'stasiun_lists.html')

class StasiunAPI(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        user = request.user
        data = ConnectDB.getAllDataWithQuery(
                '''
                SELECT * FROM stasiun
                '''
            )
        return Response(data)

def stasiun_lists(request):
    person = ConnectDB.getUserDataWithApi(request)
    response = ConnectDB.getPersonalDataWithApi(request, 'stasiun', '/stasiun/api/')
    print(response)
    response.update(person)
    return render(request, 'stasiun.html', response)

def add_stasiun(request):
    if (request.method == "POST"):
        id = random.randint(0, 100000)
        nama = request.POST.get('nama', None)
        alamat = request.POST.get('alamat', None)
        latitude = request.POST.get('latitude', None)
        longitude = request.POST.get('longitude', None)
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO stasiun VALUES(%s, %s, %s, %s, %s)", [
                id, alamat, latitude, longitude, nama])
        return HttpResponse("SUCCESS 200")
    else:
        return HttpResponse("HTTP 204")