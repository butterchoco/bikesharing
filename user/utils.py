from bikesharing.utils.decouple import config


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
