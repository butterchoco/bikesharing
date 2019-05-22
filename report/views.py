from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from user.utils import ConnectDB
import requests
# Create your views here.


class ReportAPI(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        user = request.user
        with connection.cursor() as cursor:
            if (user.email == "ANGGOTA"):
                cursor.execute(
                    "SELECT * FROM anggota a, laporan t, person p WHERE p.ktp = a.ktp AND a.no_kartu = t.no_kartu_anggota AND p.ktp = %s", [user.username])
                return Response(ConnectDB.dictfetchall(cursor))


def report_view(request):
    response = {}
    headers = {'Authorization': 'Token ' + request.session['token']}
    dataLaporan = requests.get(
        ConnectDB.BASE_URL + '/report/api/', headers=headers).json()
    response.update(dataLaporan[0])
    if (len(dataLaporan) == 0):
        dataPerson = requests.get(
            ConnectDB.BASE_URL + '/user/api/', headers=headers).json()
        response.update(dataPerson[0])
    return render(request, 'report.html', response)
