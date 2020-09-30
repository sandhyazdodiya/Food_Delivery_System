from rest_framework import serializers
from app.models.restaurant import *
from app.models.delivery import DeliveryPerson
from app.models.customer import Customer
from app.models.admin import Admin
from custom_user.serializers import *
from custom_user.models import *

class RestaurantProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Restaurant
        fields = ['user','name','description','city','state','country']
    def create(self, validated_data):
        user_data = dict(validated_data.pop('user'))
        user = User.objects.create_user(**user_data)
        restaurant = Restaurant.objects.create(user=user,**validated_data)
        return restaurant


class DeliveryPersonProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = DeliveryPerson
        fields = ['user','name','description','city','state','country']
    def create(self, validated_data):
        user_data = dict(validated_data.pop('user'))
        user = User.objects.create_user(**user_data)
        delivery_person = DeliveryPerson.objects.create(user=user,**validated_data)
        return delivery_person

class CustomerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Customer
        fields = ['user','city','state','country']
    def create(self, validated_data):
        user_data = dict(validated_data.pop('user'))
        user = User.objects.create_user(**user_data)
        customer = Customer.objects.create(user=user,**validated_data)
        return customer 

class AdminProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Admin
        fields = ['user','city','state','country']
    def create(self, validated_data):
        user_data = dict(validated_data.pop('user'))
        user = User.objects.create_superuser(**user_data)
        admin = Admin.objects.create(user=user,**validated_data)
        return admin 

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=FoodItem
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields='__all__'