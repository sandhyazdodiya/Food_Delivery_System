from rest_framework import viewsets
from app.serializers import *
from app.models.restaurant import Restaurant,FoodItem
from rest_framework.response import Response
from rest_framework.parsers import FormParser,MultiPartParser
from django.views import View
from django.shortcuts import render, redirect
from custom_user.models import *
from custom_user.serializers import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from core.viewsets import *
from django.db.models import Count

class RestaurantViewset(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantProfileSerializer
    def create(self, request, *args, **kwargs):
        serializer = super().create(request, *args, **kwargs)
        return Response({"Success": "Registered Sucessfully"},)

        
class RestaurantView(View):
    
    template_name = "restaurant/restaurant-profile.html"

    def get(self, request):
        return render(request, self.template_name, locals())


class FoodItemViewset(ViewSetPatch,viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    parser_classes = (FormParser, MultiPartParser)
    def create(self, request, *args, **kwargs):
        #To make Query dict mutable
        request.POST._mutable = True
        user_id=self.request.user.id
        print(request)
        restaurant=Restaurant.objects.filter(user_id=user_id).values('id').last()
        restaurant_id=restaurant.get("id")
        request.data['restaurant'] = restaurant_id
        print(request.data)
        return super().create(request, *args, **kwargs)
       


class RestaurantMenuView(LoginRequiredMixin,View):
    """
    Render Restaurant Menu page for customer.
    It displays list of food items

    :param request:
    :param restaurant_id:
    :return:
    """
    template_name = "customer/restaurant-menu.html"
    
    def get(self, request,restaurant_id=None):
        cart=request.session.get('cart')
        if not cart:
            request.session["cart"]= {}
        fooditems=FoodItem.objects.filter(restaurant_id=restaurant_id)
        restaurant=Restaurant.objects.get(id=restaurant_id)
        return render(request, self.template_name, locals())


class RestaurantDashaboard(View):
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
    
    template_name = "restaurant/update-create-food.html"

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

class FoodsView(View):
    
    template_name = "restaurant/foods.html"
    
    def get(self, request):
        user_id=request.user.id
        restaurant=Restaurant.objects.get(user_id=user_id)
        foods=FoodItem.objects.filter(restaurant_id=restaurant.id)
        return render(request, self.template_name, locals())
        
class RestaurantOrders(LoginRequiredMixin,View):
    """
    Render Restaurant Orders page.
    It displays list of orders

    :param request:
    :return:
    """
    
    template_name = "restaurant/restaurant-orders.html"

    def get(self, request):
        user_id=request.user.id
        restaurant=Restaurant.objects.get(user_id=user_id)
        # foods=FoodItem.objects.filter(restaurant_id=restaurant.id).values_list('id', flat=True)
        # orderitems=OrderItem.objects.filter(food_id__in=foods).values_list('order_id',flat=True).distinct()

        foods=FoodItem.get_fooditems_by_restaurant(restaurant.id)
        print(foods)
        orderitems=OrderItem.objects.filter(food_id__in=foods)

        print(orderitems)
        # orderitems=OrderItem.objects.filter(food_id__in=foods).values_list('food_id',flat=True)
        # orderedfoods=FoodItem.objects.filter(id__in=orderitems)
        return render(request, self.template_name, locals())