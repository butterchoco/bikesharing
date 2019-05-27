from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import signup_form
import simplejson
import random
# ViewSets define the view behavior.


# Create your views here.

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
            cursor.execute("INSERT INTO public.person VALUES(%s, %s, %s, %s, %s, %s, %s)", [
                ktp, email, nama, alamat, tgl_lahir, no_telp, role])
            if (role == "ADMIN"):
                cursor.execute(
                    "INSERT INTO public.admin VALUES(%s)", [ktp])
            elif (role == "ANGGOTA"):
                id = random.randint(0, 100000)
                cursor.execute(
                    "INSERT INTO public.anggota VALUES(%s, 0, 0, %s)", [str(id) + ktp[:4], ktp])
            else:
                cursor.execute(
                    "INSERT INTO public.PETUGAS VALUES(%s, 30000)", [ktp])
        return HttpResponse("SUCCESS 200")
    else:
        return HttpResponse("HTTP 204")


def login(request):
    if (request.method == "POST"):
        ktp = request.POST.get('ktp', False)
        email = request.POST.get('email', False)
        data = {}
        with connection.cursor() as cursor:
            try:
                cursor.execute(
                    "SELECT ktp, nama, role from public.person where ktp = %s AND email = %s", [ktp, email])
                person = cursor.fetchone()
                if (person[2] == "ANGGOTA"):
                    cursor.execute(
                        "SELECT * from public.anggota where ktp = %s", [ktp])
                    json = cursor.fetchone()
                    request.session['no_kartu'] = json[0]
                    request.session['saldo'] = json[1]
                    request.session['poin'] = json[2]
                elif (person[2] == "PETUGAS"):
                    cursor.execute(
                        "SELECT * from public.petugas where ktp = %s", [ktp])
                    json = cursor.fetchone()
                    request.session['gaji'] = json[1]
                request.session['ktp'] = person[0]
                request.session['nama'] = person[1]
                request.session['role'] = person[2]
                data['ktp'] = request.session['ktp']
                data['role'] = request.session['role']
                taken = True
            except:
                taken = False
            finally:
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
            try:
                cursor.execute(
                    "SELECT ktp, nama, role from public.person where ktp = %s OR email = %s", [ktp, email])
                person = cursor.fetchone()
                if (person[2] == "ANGGOTA"):
                    cursor.execute(
                        "SELECT * from public.anggota where ktp = %s", [ktp])
                    json = cursor.fetchone()
                elif (person[2] == "PETUGAS"):
                    cursor.execute(
                        "SELECT * from public.petugas where ktp = %s", [ktp])
                    json = cursor.fetchone()
                taken = True
            except:
                taken = False
            finally:
                data['is_taken'] = taken
                return JsonResponse(data)
    else:
        return HttpResponse("HTTP 204")


def logout(request):
    request.session.flush()
    return HttpResponseRedirect("/")
