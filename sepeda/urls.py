from django.urls import path
from .views import index, sepeda_lists

app_name = 'sepeda'
urlpatterns = [
    path('', index, name='sepeda'),
    path('lists', sepeda_lists, name='sepeda_lists'),
]
