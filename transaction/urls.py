from django.urls import path
from .views import transaction_view, TransactionAPI, add_transaction

app_name = 'transaction'
urlpatterns = [
    path('', transaction_view),
    path('add/', add_transaction),
    path('api/', TransactionAPI.as_view())
]
