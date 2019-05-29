from django.urls import path
from .views import signUp, login, validate, logout, PersonAPI

app_name = "registrasi"
urlpatterns = [
    path('signing+up/', signUp),
    path('authenticating/', login),
    path('validating/', validate),
    path('logout/', logout),
    path('api/', PersonAPI.as_view())
]
