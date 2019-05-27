from django.urls import path
from .views import voucher_view, VoucherAPI
app_name = 'voucher'
urlpatterns = [
    path('', voucher_view),
    path('api/', VoucherAPI.as_view())
]