from rest_framework import serializers
from .models import User
from django.core import exceptions
import django.contrib.auth.password_validation as validators


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'is_superuser','user_type','phone']

