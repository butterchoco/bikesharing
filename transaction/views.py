from django.shortcuts import render

# Create your views here.

response = {}


def transaction_view(request):
    if ('ktp' in request.session.keys()):
        response['ktp'] = request.session['ktp']
        response['nama'] = request.session['nama']
        response['role'] = request.session['role']
        if (request.session['role'] == "ANGGOTA"):
            response['no_kartu'] = request.session['no_kartu']
            response['saldo'] = request.session['saldo']
            response['poin'] = request.session['poin']
        elif (request.session['role'] == "PETUGAS"):
            response['gaji'] = request.session['gaji']

    return render(request, 'transaction.html', response)
