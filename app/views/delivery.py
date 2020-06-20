from rest_framework import viewsets
from app.serializers import *
from app.models.delivery import DeliveryPerson
from rest_framework.response import Response
from django.views import View
from django.shortcuts import render, redirect
from custom_user.models import *
from custom_user.serializers import *
class DeliveryPersonViewset(viewsets.ModelViewSet):
    queryset = DeliveryPerson.objects.all()
    serializer_class = DeliveryPersonProfileSerializer
    def create(self, request, *args, **kwargs):
        serializer = super().create(request, *args, **kwargs)
        return Response({"Success": "Registered Sucessfully"},)
