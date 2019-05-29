from django.urls import path
from .views import add_sepeda, delete_sepeda, update_sepeda, sepeda_lists, SepedaAPI

app_name = 'sepeda'
urlpatterns = [
    path('add/', add_sepeda, name='sepeda'),
    path('', sepeda_lists, name='sepeda_lists'),
    path('api/', SepedaAPI.as_view()),
    path('delete/', delete_sepeda, name='delete_sepeda'),
    path('update/', update_sepeda, name='update_sepeda')
]
