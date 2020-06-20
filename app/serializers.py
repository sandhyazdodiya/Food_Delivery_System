from rest_framework import serializers
from app.models.restaurant import Restaurant
from app.models.delivery import DeliveryPerson
from custom_user.serializers import *
from custom_user.models import *

class RestaurantProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Restaurant
        fields = ['user','name','description','city','state','country']
    def create(self, validated_data):
        user_data = dict(validated_data.pop('user'))
        user = User.objects.create_superuser(**user_data)
        restaurant = Restaurant.objects.create(user=user,**validated_data)
        return restaurant
class DeliveryPersonProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = DeliveryPerson
        fields = ['user','name','description','city','state','country']
    def create(self, validated_data):
        user_data = dict(validated_data.pop('user'))
        user = User.objects.create_superuser(**user_data)
        delivery_person = DeliveryPerson.objects.create(user=user,**validated_data)
        return delivery_person