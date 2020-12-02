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

    def __str__(self):
        return self.name

    @staticmethod
    def get_restaurant_by_id(ids):
        return Restaurant.objects.filter(id__in =ids)

    @staticmethod
    def get_restaurant_by_user_id(id):

        try:
            return Restaurant.objects.get(user_id =id)
        except:
            return False


# model for FoodItem
class FoodItem(models.Model):
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=200)
    price=models.IntegerField()
    isnonveg=models.BooleanField(default=False)
    image = models.FileField(upload_to='documents/',null=True,blank=True,)
    restaurant=models.ForeignKey(Restaurant,on_delete = models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'restaurant_id'], name='unique_food_name')
        ]

    @staticmethod
    def get_fooditems_by_id(ids):
        return FoodItem.objects.filter(id__in =ids)

    @staticmethod
    def get_fooditems_by_restaurant(id):
        return FoodItem.objects.filter(restaurant_id =id)

#model for Order      
class Order(models.Model):

    STATUS = (
        ('Placed', 'Placed'),
        ('Accepted', 'Accepted'),
        ('Processed', 'Processed'),
        ('Pickup', 'Pickup'),
        ('Delivered', 'Delivered'),
    )

    customer=models.ForeignKey(Customer,on_delete = models.CASCADE)
    status=models.CharField(max_length=20,choices=STATUS)
    price=models.IntegerField(null=True)

#model for OrderItem
class OrderItem(models.Model):
    
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    food=models.ForeignKey(FoodItem,on_delete=models.CASCADE)
    quantity=models.IntegerField(null=True)
    status=models.CharField(max_length=20,null=True)
    price=models.IntegerField(null=True)

    def get_orderitems_by_order_id(order_id):
        return OrderItem.objects.filter(order_id=order_id)