from bikesharing.utils.decouple import config
from django.db import connection
import requests

class ConnectDB:
    PRODUCTION = config('PRODUCTION') == 'ON'
    if (PRODUCTION):
        BASE_URL = 'http://c6-basdat-bikesharing.herokuapp.com'
    else:
        BASE_URL = 'http://127.0.0.1:8000'

    def dictfetchall(cursor):
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    def getPersonalDataWithApi(request, title, pattern):
        response = {}
        response[title] = []
        headers = {'Authorization': 'Token ' + request.session['token']}
        data = requests.get(ConnectDB.BASE_URL + pattern, headers=headers).json()
        for record in data:
            response[title].append(record)
        return response

    def getUserDataWithApi(request):
        headers = {'Authorization': 'Token ' + request.session['token']}
        person = requests.get(ConnectDB.BASE_URL + '/user/api/', headers=headers).json()
        return person[0]

    def getAllDataWithQuery(query):
        with connection.cursor() as cursor:
            cursor.execute(query)
            return ConnectDB.dictfetchall(cursor)
    
    def getDataWithQuery(query, ktp):
        with connection.cursor() as cursor:
            cursor.execute(query, ktp)
            return ConnectDB.dictfetchall(cursor)