from django.shortcuts import render

# Create your views here.


def penugasan_view(request):
    return render(request, 'penugasan.html')


def update_penugasan_view(request):
    return render(request, 'updatepenugasan.html')


def show_penugasan_table_view(request):
    return render(request, 'tabelpenugasan.html')
