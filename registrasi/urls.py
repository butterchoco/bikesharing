from django.urls import path
from .views import signUp

app_name="registrasi"
urlpatterns = [
    path('', signUp)
]