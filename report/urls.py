from django.urls import path
from .views import report_view, ReportAPI

app_name = 'report'
urlpatterns = [
    path('', report_view),
    path('api/', ReportAPI.as_view())
]
