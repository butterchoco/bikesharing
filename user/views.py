from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .utils import ConnectDB
import simplejson
import random
import requests


class PersonAPI(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        user = request.user
        with connection.cursor() as cursor:
            if (user.email == "ANGGOTA"):
                cursor.execute(
                    "SELECT * FROM person p, anggota a WHERE p.ktp = a.ktp AND p.ktp = %s", [user.username])
                return Response(ConnectDB.dictfetchall(cursor))
            elif (user.email == "PETUGAS"):
                cursor.execute(
                    "SELECT * FROM person p, petugas a WHERE p.ktp = a.ktp AND p.ktp = %s", [user.username])
                return Response(ConnectDB.dictfetchall(cursor))
            elif (user.email == "ADMIN"):
                cursor.execute(
                    "SELECT * FROM person p, admin a WHERE p.ktp = a.ktp AND p.ktp = %s", [user.username])
                return Response(ConnectDB.dictfetchall(cursor))
            else:
                return HttpResponse("Cannot define user type.")


def signUp(request):
    if (request.method == "POST"):
        ktp = request.POST.get('ktp', None)
        email = request.POST.get('email', None)
        nama = request.POST.get('nama', None)
        alamat = request.POST.get('alamat', None)
        tgl_lahir = request.POST.get('tgl_lahir', None)
        no_telp = request.POST.get('no_telp', None)
        role = request.POST.get('role', None)
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO person VALUES(%s, %s, %s, %s, %s, %s, %s)", [
                ktp, email, nama, alamat, tgl_lahir, no_telp, role])
            if (role == "ADMIN"):
                cursor.execute(
                    "INSERT INTO admin VALUES(%s)", [ktp])
            elif (role == "ANGGOTA"):
                id = random.randint(0, 100000)
                cursor.execute(
                    "INSERT INTO anggota VALUES(%s, 0, 0, %s)", [str(id) + ktp[:4], ktp])
            else:
                cursor.execute(
                    "INSERT INTO PETUGAS VALUES(%s, 30000)", [ktp])
        user = User.objects.create_user(
            username=ktp, email=role, password=email)
        Token.objects.create(user=user)
        return HttpResponse("SUCCESS 200")
    else:
        return HttpResponse("HTTP 204")


def login(request):
    if (request.method == "POST"):
        taken = False
        ktp = request.POST.get('ktp', False)
        email = request.POST.get('email', False)
        data = {}
        token = requests.post(
            ConnectDB.BASE_URL + '/auth/', {'username': ktp, 'password': email}).json()
        if ('token' in token.keys()):
            request.session['token'] = token['token']
            taken = True
        data['is_taken'] = taken
        return JsonResponse(data)
    else:
        return HttpResponse("HTTP 204")


def validate(request):
    if (request.method == "POST"):
        ktp = request.POST.get('ktp', False)
        email = request.POST.get('email', False)
        data = {}
        with connection.cursor() as cursor:
            error = ""
            taken = False
            if (ktp != ""):
                cursor.execute(
                    "SELECT ktp, nama, role from person where ktp = %s", [ktp])
                person = cursor.fetchone()
                if (person is not None):
                    error = "Ktp sudah terpakai"
                    taken = True
            elif (email != ""):
                cursor.execute(
                    "SELECT ktp, nama, role from person where email = %s", [email])
                person = cursor.fetchone()
                if (person is not None):
                    error = "Email sudah terpakai"
                    taken = True
            else:
                cursor.execute(
                    "SELECT ktp, nama, role from person where ktp = %s OR email = %s", [ktp, email])
                person = cursor.fetchone()
                if (person is not None):
                    error = "Ktp atau email sudah terpakai"
                    taken = True
            data = {
                'is_taken': taken,
                'error': error
            }
            return JsonResponse(data)
    else:
        return HttpResponse("HTTP 204")


def logout(request):
    request.session.flush()
    return HttpResponseRedirect("/")
