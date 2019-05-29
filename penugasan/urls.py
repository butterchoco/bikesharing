from django.urls import path
from .views import penugasan_view, update_penugasan_view, PenugasanAPI, add_penugasan

app_name = 'penugasan'
urlpatterns = [
    path('', penugasan_view),
    path('api/', PenugasanAPI.as_view()),
    path('add/', add_penugasan),
    path('update/', update_penugasan_view),
]
