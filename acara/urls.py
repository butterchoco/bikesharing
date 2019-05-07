from django.urls import path
from .views import acara_view, update_acara_view, show_acara_table_view

app_name = 'acara'
urlpatterns = [
    path('', acara_view),
    path('update', update_acara_view),
    path('table', show_acara_table_view)
]
