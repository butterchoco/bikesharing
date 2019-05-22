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
# Create your views here.


class TransactionAPI(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        user = request.user
        with connection.cursor() as cursor:
            if (user.email == "ANGGOTA"):
                cursor.execute(
                    "SELECT * FROM anggota a, transaksi t, person p WHERE p.ktp = a.ktp AND a.no_kartu = t.no_kartu_anggota AND p.ktp = %s", [user.username])
                return Response(ConnectDB.dictfetchall(cursor))


def transaction_view(request):
    response = {}
    headers = {'Authorization': 'Token ' + request.session['token']}
    dataTransaksi = requests.get(
        ConnectDB.BASE_URL + '/transaction/api/', headers=headers).json()
    response.update(dataTransaksi[0])
    if (len(dataTransaksi) == 0):
        dataPerson = requests.get(
            ConnectDB.BASE_URL + '/user/api/', headers=headers).json()
        response.update(dataPerson[0])
    return render(request, 'transaction.html', response)


def add_transaction(request):
    if (request.method == "POST"):
        no_kartu = request.POST.get('no_kartu', None)
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        jenis = request.POST.get('jenis', None)
        nominal = request.POST.get('nominal', None)
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO transaksi VALUES(%s, %s, %s, %s)", [
                no_kartu, date, jenis, nominal])
        return HttpResponse("SUCCESS 200")
    else:
        return HttpResponse("HTTP 204")
