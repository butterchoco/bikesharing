from django.shortcuts import render

# Create your views here.


def acara_view(request):
    return render(request, 'acara.html')


def update_acara_view(request):
    return render(request, 'updateacara.html')


def show_acara_table_view(request):
    return render(request, 'tabelacara.html')
