from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from user.utils import ConnectDB
# Create your views here.

class PenugasanAPI(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        user = request.user
        if (user.email == "ADMIN" or user.email == "PETUGAS"):
            data = ConnectDB.getDataWithQuery(
                '''
                SELECT s.* FROM penugasan s, person p
                WHERE p.ktp = s.ktp AND
                p.ktp = %s
                ''', [user.username]
            )
            return Response(data)
        else:
            return Response([{}])

def penugasan_view(request):
    person = ConnectDB.getUserDataWithApi(request)
    if (person['role'] == "ANGGOTA"):
        return redirect('/')
    else:
        response = ConnectDB.getPersonalDataWithApi(request, 'penugasan', '/penugasan/api/')
        response.update(person)
        return render(request, 'penugasan.html', response)


def update_penugasan_view(request):
    return render(request, 'updatepenugasan.html')

def add_penugasan(request):
    if (request.method == "POST"):
        no_kartu = request.POST.get('no_kartu', None)
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        jenis = request.POST.get('jenis', None)
        nominal = request.POST.get('nominal', None)
        with connection.cursor() as cursor:
            cursor.execute(
                '''
                INSERT INTO penugasan VALUES(%s, %s, %s, %s)
                ''', [no_kartu, date, jenis, nominal])
        return HttpResponse("SUCCESS 200")
    else:
        return HttpResponse("HTTP 204")