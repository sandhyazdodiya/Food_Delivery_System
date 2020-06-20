from rest_framework import viewsets
from app.serializers import *
from app.models.restaurant import Restaurant
from rest_framework.response import Response
from django.views import View
from django.shortcuts import render, redirect
from custom_user.models import *
from custom_user.serializers import *
class RestaurantViewset(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantProfileSerializer
    def create(self, request, *args, **kwargs):
        serializer = super().create(request, *args, **kwargs)
        return Response({"Success": "Registered Sucessfully"},)
class RestaurantView(View):
    
    template_name = "restaurant-profile.html"

    def get(self, request):
        return render(request, self.template_name, locals())