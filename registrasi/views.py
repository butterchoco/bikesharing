from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from .serializer import PersonSerializer
from .models import Person
from .forms import signup_form
import simplejson
import random
# ViewSets define the view behavior.


class PersonViewSet(viewsets.ModelViewSet):
    query = "SELECT * FROM public.\"PERSON\""
    queryset = Person.objects.raw(query)
    serializer_class = PersonSerializer


# Create your views here.

@csrf_exempt
def signUp(request):
    if (request.method == "POST"):
        data = simplejson.loads(request.body)
        ktp = data.get('ktp')
        email = data.get('email')
        nama = data.get('nama')
        alamat = data.get('alamat')
        tgl_lahir = data.get('tgl_lahir')
        no_telp = data.get('no_telp')
        role = data.get('role')
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM public.\"PERSON\"", )
            json = cursor.fetchall()
            if (ktp in Response(json)):
                alert("User dengan KTP tersebut sudah ada.")
                return HttpResponseRedirect('')
            else:
                cursor.execute("INSERT INTO public.\"PERSON\" VALUES(%s, %s, %s, %s, %s, %s, %s)", [
                    ktp, email, nama, alamat, tgl_lahir, no_telp, role])
                if (role == "ADMIN"):
                    cursor.execute(
                        "INSERT INTO public.\"ADMIN\" VALUES(%s)", [ktp])
                elif (role == "ANGGOTA"):
                    id = random.randint(0, 100000)
                    cursor.execute(
                        "INSERT INTO public.\"ANGGOTA\" VALUES(%s, 0, 0, %s)", [str(id) + ktp[:4], ktp])
                else:
                    cursor.execute(
                        "INSERT INTO public.\"PETUGAS\" VALUES(%s, 0)", [ktp])
                user = User.objects.create_user(ktp, email, 'admin123')
                user.save()
        return HttpResponse("SUCCESS 200")
    else:
        return HttpResponse("HTTP 204")


@csrf_exempt
def login(request):
    if (request.method == "POST"):
        form = login_form(request.POST)
        if(form.is_valid()):
            ktp = request.POST.get('ktp', False)
            email = request.POST.get('email', False)
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT cek_type_person(%s, %s)", [ktp, email])
                json = cursor.fetchone()
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
