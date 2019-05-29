from django.urls import path
from .views import voucher_view, VoucherAPI, voucher_add
app_name = 'voucher'
urlpatterns = [
    path('', voucher_view),
    path('api/', VoucherAPI.as_view()),
    path('add/', voucher_add)
]