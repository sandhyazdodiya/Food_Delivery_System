from django.db import models
from custom_user.models import *


# model for DevliveryPerson Profile
class DeliveryPerson(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,related_name='delivery_person') 
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=200)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_delivery_person_by_user_id(id):
        
        try:
            return DeliveryPerson.objects.get(user_id =id)
        except:
            return False
