from django.urls import path
from .views import index, stasiun_lists

app_name = 'stasiun'
urlpatterns = [
    path('', index, name='stasiun'),
    path('lists', stasiun_lists, name='stasiun_lists'),
]
