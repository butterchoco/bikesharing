class ConnectDB:
    BASE_URL = 'http://127.0.0.1:8000'

    def dictfetchall(cursor):
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
