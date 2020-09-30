from rest_framework import viewsets
from app.serializers import *
from app.models.restaurant import Restaurant,FoodItem
from rest_framework.response import Response
from django.views import View
from django.shortcuts import render, redirect
from custom_user.models import *
from custom_user.serializers import *
from django.contrib.auth.mixins import LoginRequiredMixin
from core.viewsets import *

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


class FoodItemViewset(ViewSetPatch,viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    def create(self, request, *args, **kwargs):
        user_id=self.request.user.id
        restaurant=Restaurant.objects.filter(user_id=user_id).values('id').last()
        restaurant_id=restaurant.get("id")
        request.data['restaurant'] = restaurant_id
        return super().create(request, *args, **kwargs)
       


class RestaurantMenuView(LoginRequiredMixin,View):
    """
    Render Restaurant Menu page for customer.
    It displays list of food items

    :param request:
    :param restaurant_id:
    :return:
    """

    template_name = "restaurant-menu.html"

    def get(self, request,restaurant_id=None):
        fooditems=FoodItem.objects.filter(restaurant_id=restaurant_id)
        restaurant=Restaurant.objects.get(id=restaurant_id)
        return render(request, self.template_name, locals())


class RestaurantDashaboard(LoginRequiredMixin,View):
    """
    Render Restaurant Dashboard page.
    It displays list of food items

    :param request:
    :return:
    """
    
    template_name = "restaurant/restaurant-dashboard.html"

    def get(self, request):
        user_id=request.user.id
        restaurant=Restaurant.objects.get(user_id=user_id)
        foods=FoodItem.objects.filter(restaurant_id=restaurant.id)
        return render(request, self.template_name, locals())

class FoodItemView(View):
    
    template_name = "restaurant/view-create-food.html"

    def get(self, request, food_id=None):
        """
        Render the Food page.
        It displays the create and update page

        :param request:
        :param food_id:
        :return:
        """

        if food_id:
            try:
                food = FoodItem.objects.get(id=food_id)
                action = "edit"
            except FoodItem.DoesNotExist:
                return redirect("restaurant-dashboard")
        else:
            action = "create"
        return render(request, self.template_name, locals())

class RestaurantOrders(LoginRequiredMixin,View):
    """
    Render Restaurant Dashboard page.
    It displays list of food items

    :param request:
    :return:
    """
    
    template_name = "restaurant/restaurant-orders.html"

    def get(self, request):
        user_id=request.user.id
        restaurant=Restaurant.objects.get(user_id=user_id)
        foods=FoodItem.objects.filter(restaurant_id=restaurant.id).values_list('id', flat=True)
        orderitems=OrderItem.objects.filter(food_id__in=foods).values_list('order_id',flat=True).distinct()
        # orderitems=OrderItem.objects.filter(food_id__in=foods).values_list('food_id',flat=True)
        # orderedfoods=FoodItem.objects.filter(id__in=orderitems)
        return render(request, self.template_name, locals())