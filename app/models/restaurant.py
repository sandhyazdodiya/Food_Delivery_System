from django.db import models
from custom_user.models import *
# Create your models here.
class Restaurant(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,related_name='restaurant_owner') 
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=200)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
