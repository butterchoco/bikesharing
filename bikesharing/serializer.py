from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import connection
from registrasi.models import Person

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('ktp', 'email', 'nama', 'alamat', 'tgl_lahir', 'no_telp')