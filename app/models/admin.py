from django.db import models
from custom_user.models import *


# model for Customer Profile
class Admin(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,related_name='admin') 
    name=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    
    @staticmethod
    def get_admin_by_user_id(id):
        
        try:
            return Admin.objects.get(user_id =id)
        except:
            return False
    