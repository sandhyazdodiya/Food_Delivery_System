from django.db import models
from custom_user.models import *


# model for Customer Profile
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,related_name='customer') 
    name=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    
    
    def get_customer_by_user_id(user_id):
        
        try:
            return Customer.objects.get(user_id=user_id)
        except:
            return False



    


