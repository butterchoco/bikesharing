from django.urls import path
from .views import penugasan_view, update_penugasan_view, show_penugasan_table_view

app_name = 'penugasan'
urlpatterns = [
    path('', penugasan_view),
    path('update', update_penugasan_view),
    path('table', show_penugasan_table_view)
]
