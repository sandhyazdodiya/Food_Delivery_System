from django.db import models
from custom_user.models import *
from app.models.customer import *

# model for Restaurant Profile
class Restaurant(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,related_name='restaurant_owner') 
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=200)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)

# model for FoodItem
class FoodItem(models.Model):
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=200)
    price=models.IntegerField()
    restaurant=models.ForeignKey(Restaurant,on_delete = models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'restaurant_id'], name='unique_food_name')
        ]
    
#model for Order
class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete = models.CASCADE)
    status=models.CharField(max_length=20)
    charge=models.IntegerField(null=True)

#model for OrderItem
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    food=models.ForeignKey(FoodItem,on_delete=models.CASCADE)
    quantity=models.IntegerField(null=True)