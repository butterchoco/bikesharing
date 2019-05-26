from django.urls import path
from .views import index
app_name = 'voucher'
urlpatterns = [
    path('', index),
]