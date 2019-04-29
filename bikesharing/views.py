from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializer import UserSerializer, PersonSerializer
from registrasi.models import Person

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.raw('''SELECT * FROM "public"."PERSON"''')
    serializer_class = PersonSerializer