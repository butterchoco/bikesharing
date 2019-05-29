from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from user.utils import ConnectDB

# Create your views here.


class ReportAPI(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        user = request.user
        if (user.email == "ADMIN" or user.email == "PETUGAS"):
            data = ConnectDB.getDataWithQuery(
                    '''
                    SELECT l.*
                    FROM anggota a, laporan l, person p
                    WHERE p.ktp = a.ktp AND a.no_kartu = l.no_kartu_anggota AND p.ktp = %s
                    ''', [user.username])
            return Response(data)
        else:
            return Response([{}])

def report_view(request):
    person = ConnectDB.getUserDataWithApi(request)
    print(person['role'])
    if (person['role'] == "ANGGOTA"):
        return redirect('/')
    else:
        response = ConnectDB.getPersonalDataWithApi(request, 'laporan', '/report/api/')
        response.update(person)
        return render(request, 'report.html', response)
