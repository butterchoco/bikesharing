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


class VoucherAPI(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        user = request.user
        if (user.email == 'ADMIN' or user.email == 'PETUGAS' or user.email == 'ANGGOTA'):
            data = ConnectDB.getDataWithQuery(
                '''
                SELECT v.*
                FROM anggota a, voucher v, person p
                WHERE p.ktp = a.ktp AND a.no_kartu = v.no_kartu_anggota AND p.ktp = %s
                ''', [user.username])
            return Response(data)
        else:
            return Response([{}])


def voucher_view(request):
    person = ConnectDB.getUserDataWithApi(request)
    response = ConnectDB.getPersonalDataWithApi(request, 'voucher', '/voucher/api/')
    response.update(person)
    return render(request, 'voucher_view.html', response)

def voucher_add(request):
    if (request.method == "POST"):
        id_voucher = request.POST.get('id_voucher', None)
        nama = request.POST.get('nama', None)
        kategori = request.POST.get('kategori', None)
        nilai_poin = request.POST.get('nilai_poin', None)
        deskripsi = request.POST.get('deskripsi', None)
        # no_kartu_anggota = request.POST.get('no_kartu_anggota', None)
        with connection.cursor() as cursor:
            cursor.execute(
                '''
                INSERT INTO voucher VALUES(%s, %s, %s, %s, %s)
                ''', [id_voucher, nama, kategori, nilai_poin, deskripsi])
        return HttpResponse("SUCCESS 200")
    else:
        return HttpResponse("HTTP 204")