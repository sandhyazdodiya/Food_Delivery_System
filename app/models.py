from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Photo(models.Model):
  image = CloudinaryField('image')

class Friend(models.Model):
    name = models.CharField(max_length=100)

class Belonging(models.Model):
    name = models.CharField(max_length=100)

class Borrowed(models.Model):
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)
