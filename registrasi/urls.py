from django.urls import path
from .views import signUp, login

app_name = "registrasi"
urlpatterns = [
    path('signing+up/', signUp),
    path('authenticating/', login)
]
