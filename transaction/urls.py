from django.urls import path
from .views import transaction_view, TransactionAPI

app_name = 'transaction'
urlpatterns = [
    path('', transaction_view),
    path('api/', TransactionAPI.as_view())
]
