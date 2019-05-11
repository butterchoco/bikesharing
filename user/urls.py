from django.urls import path
from .views import signUp, login, validate, logout, personAPI

app_name = "registrasi"
urlpatterns = [
    path('signing+up/', signUp),
    path('authenticating/', login),
    path('validating/', validate),
    path('logout/', logout),
    path('person/', personAPI)
]
