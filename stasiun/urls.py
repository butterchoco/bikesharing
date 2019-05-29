from django.urls import path
from .views import add_stasiun, stasiun_lists, StasiunAPI

app_name = 'stasiun'
urlpatterns = [
    path('api/', StasiunAPI.as_view()),
    path('add/', add_stasiun, name='stasiun'),
    path('', stasiun_lists, name='stasiun_lists'),
]
