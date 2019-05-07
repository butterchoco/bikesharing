from django.shortcuts import render

# Create your views here.


def report_view(request):
    return render(request, 'report.html')
