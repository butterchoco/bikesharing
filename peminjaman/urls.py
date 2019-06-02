from django.urls import path
from .views import peminjaman_view, peminjaman_add, PeminjamanAPI

app_name = 'peminjaman'
urlpatterns = [
    path('', peminjaman_view),
    path('add/', peminjaman_add),
    path('api/', PeminjamanAPI.as_view()),
]