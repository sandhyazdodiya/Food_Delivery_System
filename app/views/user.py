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
from core.utils import *

class UserDashboardView(LoginRequiredMixin,View):
    
    template_name = "customer/dashboard.html"

    def get(self, request):
        print("from session",request.session.get('customer_id'))
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
        food_id=request.data.get("food_id",None)
        action=request.data.get("action",None)
        if food_id is not None or action is not None:
            cart=request.session.get("cart")
            if cart:
                quantity = cart.get(food_id)
                if quantity:
                    if action =="remove":
                        if quantity<=1:
                            cart.pop(food_id)
                        else:
                            cart[food_id] = quantity-1
                    else:
                        cart[food_id] = quantity+1
                else:
                    cart[food_id] = 1
            else:
                cart = {}
                cart[food_id] = 1

            request.session['cart'] = cart
            return success_response('Added Successfully')
        else:
            return error_response('Error While adding into cart',None,status.HTTP_400_BAD_REQUEST)

class UserOrdersView(LoginRequiredMixin,View):
    
    template_name = "customer/user-orders.html"

    def get(self, request):
        customer_id=request.user.id
        customer=Customer.objects.get(user_id=customer_id)
        orders=Order.objects.filter(customer=customer)
        return render(request, self.template_name, locals())



class CartView(LoginRequiredMixin,View):
    
    template_name = "customer/cart.html"

    def get(self, request):
        cart=request.session.get('cart')
        ids = list(cart.keys())
        fooditems = FoodItem.get_fooditems_by_id(ids)
        return render(request, self.template_name, locals())

class PlaceOrderAPIView(APIView):
    def post(self,request):
        customer_id=request.session.get("customer_id",None)
        cart = request.session.get('cart',None)
        price=request.data.get("price",None)
        if price and cart and customer_id:
            fooditems = FoodItem.get_fooditems_by_id(list(cart.keys()))
            order=Order(customer=Customer(customer_id),
                        status="active",
                        price=price )
            order.save()
            for fooditem in fooditems:
                print(cart.get(str(fooditem.id)))
                orderitem = OrderItem(order=order,
                            food=fooditem,
                            quantity=cart.get(str(fooditem.id)),
                            status="active",
                            price=fooditem.price)
                orderitem.save()
            request.session['cart'] = {}
            return success_response('Order created successfully')
        else:
            return error_response('Error While Placing order',None,status.HTTP_400_BAD_REQUEST)