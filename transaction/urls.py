from django.urls import path
from .views import transaction_view

app_name = 'transaction'
urlpatterns = [
    path('', transaction_view)
]
