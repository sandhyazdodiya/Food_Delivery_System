from rest_framework import viewsets
from app.serializers import *
from app.models.restaurant import Restaurant,Order,OrderItem,FoodItem
from app.models.customer import Customer
from rest_framework.response import Response
from django.views import View
from django.shortcuts import render, redirect,get_object_or_404
from custom_user.models import *
from custom_user.serializers import *
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView

class UserDashboardView(LoginRequiredMixin,View):
    
    template_name = "dashboard.html"

    def get(self, request):
        restaurants=Restaurant.objects.all()
        return render(request, self.template_name, locals())


class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerProfileSerializer
    def create(self, request, *args, **kwargs):
        serializer = super().create(request, *args, **kwargs)
        return Response({"Success": "Registered Sucessfully"},)


class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewset(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class AddtoCartViewSet(APIView):
    def post(self,request):
        customer_id=request.user.id
        food_id=request.data["id"]
        customer=Customer.objects.get(user_id=customer_id)
        food=FoodItem.objects.get(id=food_id)
        print(customer)
        order,created = Order.objects.get_or_create(customer=customer, status="active")
        orderItem=OrderItem.objects.create(order=order,food=food)
        return Response({"Success": "added Sucessfully"},)

class UserOrdersView(LoginRequiredMixin,View):
    
    template_name = "my-orders.html"

    def get(self, request):
        customer_id=request.user.id
        customer=Customer.objects.get(user_id=customer_id)
        orders=Order.objects.filter(customer=customer)
        return render(request, self.template_name, locals())