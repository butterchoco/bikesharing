from django.shortcuts import render
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
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT v.* FROM voucher v, person p WHERE p.ktp = %s", [user.username])
            return Response(ConnectDB.dictfetchall(cursor))


def voucher_view(request):
    response = {}
    # headers = {'Authorization': 'Token ' + request.session['token']}
    dataVoucher = requests.get(
        ConnectDB.BASE_URL + '/voucher/api/').json()
    dataPerson = requests.get(
        ConnectDB.BASE_URL + '/user/api/').json()
    # response.update(dataPerson[0])
    response['voucher'] = []
    for data in dataVoucher:
        response['voucher'].append(data)
    return render(request, 'voucher_view.html', response)
