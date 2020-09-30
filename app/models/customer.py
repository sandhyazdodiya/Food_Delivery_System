from django.db import models
from custom_user.models import *


# model for Customer Profile
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,related_name='customer') 
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    
