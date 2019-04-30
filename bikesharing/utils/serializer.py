from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import connection

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
