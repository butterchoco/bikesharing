from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializer import PersonSerializer
from .models import Person
from .forms import signup_form
# ViewSets define the view behavior.


class PersonViewSet(viewsets.ModelViewSet):
    query = "SELECT * FROM public.\"PERSON\""
    queryset = Person.objects.raw(query)
    serializer_class = PersonSerializer


# Create your views here.
no_kartu = 1


def signUp(request):
    if (request.method == "POST"):
        form = signup_form(request.POST)
        if (form.is_valid()):
            ktp = request.POST.get('ktp', False)
            email = request.POST.get('email', False)
            nama = request.POST.get('nama', False)
            alamat = request.POST.get('alamat', False)
            tgl_lahir = request.POST.get('tgl_lahir', False)
            no_telp = request.POST.get('no_telp', False)
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM public.\"PERSON\"", )
                json = cursor.fetchall()
                if (ktp in Response(json)):
                    alert("User dengan KTP tersebut sudah ada.")
                    return HttpResponseRedirect('')
                else:
                    cursor.execute("INSERT INTO public.\"PERSON\" VALUES(%s, %s, %s, %s, %s, %s)", [
                        ktp, email, nama, alamat, tgl_lahir, no_telp])
                    if (role == "ADMIN"):
                        cursor.execute(
                            "INSERT INTO public.\"ADMIN\" VALUES(%s)", [ktp])
                    elif (role == "ANGGOTA"):
                        cursor.execute(
                            "INSERT INTO public.\"ANGGOTA\" VALUES(%s, 0, 0, %s)", [no_kartu, ktp])
                        no_kartu += 1
                    else:
                        cursor.execute(
                            "INSERT INTO public.\"PETUGAS\" VALUES(%s, 0)", [ktp])
                    user = User.objects.create_user(ktp, email, 'admin123')
                    user.save()
            return HttpResponseRedirect('')
        else:
            return HttpResponse("INVALID 500")
    else:
        return HttpResponse("HTTP 204")


def login(request):
    if (request.method == "POST"):
        form = login_form(request.POST)
        if(form.is_valid()):
            ktp = request.POST.get('ktp', False)
            email = request.POST.get('email', False)
            role = request.POST.get('role', False)
            with connection.cursor() as cursor:
                if (role == "ADMIN"):
                    cursor.execute("SELECT * FROM public.\"ADMIN\"", )
                elif (role == "ANGGOTA"):
                    cursor.execute("SELECT * FROM public.\"ANGGOTA\"", )
                elif (role == "PETUGAS"):
                    cursor.execute("SELECT * FROM public.\"PETUGAS\"", )
                json = cursor.fetchall()
                if (ktp in Response(json)):
                    user = authenticate(
                        request, username=ktp, password='test123')
                    if (user is not None):
                        login(request, user)
                        return HttpResponseRedirect('')
                alert("Ktp belum terdaftar")
        else:
            return HttpResponse("INVALID 500")
    else:
        return HttpResponse("HTTP 204")
