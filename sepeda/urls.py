from django.urls import path
from .views import add_sepeda, sepeda_lists, SepedaAPI

app_name = 'sepeda'
urlpatterns = [
    path('add/', add_sepeda, name='sepeda'),
    path('', sepeda_lists, name='sepeda_lists'),
    path('api/', SepedaAPI.as_view())
]
