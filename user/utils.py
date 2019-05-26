class ConnectDB:
    BASE_URL = 'http://c6-basdat-bikesharing.herokuapp.com'

    def dictfetchall(cursor):
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
