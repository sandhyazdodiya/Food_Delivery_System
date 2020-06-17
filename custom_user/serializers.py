from rest_framework import serializers
from .models import *
from django.core import exceptions
import django.contrib.auth.password_validation as validators
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 
    def create(self, validated_data):
        user = User(email=validated_data['email'],user_type=validated_data['user_type'])
        user.set_password(validated_data['password'])
        user.save()
        return user
