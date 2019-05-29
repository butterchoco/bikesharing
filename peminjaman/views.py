from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import connection
# from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from user.utils import ConnectDB

# from datetime import datetime
import requests


class PeminjamanAPI(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        user = request.user
        if user.email == 'ADMIN' or user.email == 'PETUGAS' or user.email == 'ANGGOTA':
            data = ConnectDB.getDataWithQuery(
                '''
                SELECT m.*
                FROM anggota a, peminjaman m, person p
                WHERE p.ktp = a.ktp AND a.no_kartu = m.no_kartu_anggota AND p.ktp = %s
                ''', [user.username])
            return Response(data)
        else:
            return Response([{}])


def peminjaman_view(request):
    person = ConnectDB.getUserDataWithApi(request)
    response = ConnectDB.getPersonalDataWithApi(request, 'peminjaman', '/peminjaman/api/')
    response.update(person)
    return render(request, 'peminjaman.html', response)

def peminjaman_add(request):
    if (request.method == "POST"):
        no_kartu_anggota = request.POST.get('id_voucher', None)
        datetime_pinjam = request.POST.get('nama', None)
        datetime_kembali = request.POST.get('kategori', None)
        biaya = request.POST.get('nilai_poin', None)
        denda = request.POST.get('deskripsi', None)
        nomor_sepeda = request.POST.get('no_kartu_anggota', None)
        id_stasiun = request.POST.get('no_kartu_anggota', None)
        with connection.cursor() as cursor:
            cursor.execute(
                '''
                INSERT INTO peminjaman VALUES(%s, %s, %s, %s, %s, %s, %s)
                ''', [no_kartu_anggota, datetime_pinjam, datetime_kembali, biaya, denda, nomor_sepeda,id_stasiun])
        return HttpResponse("SUCCESS 200")
    else:
        return HttpResponse("HTTP 204")