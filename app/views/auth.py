from django import forms
from django.http import HttpResponse 
from rest_framework import viewsets
from custom_user.serializers import UserSerializer
from custom_user.models import *
from custom_user.serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import status
from django.views import View
from django.shortcuts import render, redirect
from .user import *
from app.models.admin import Admin
from core.utils import *
from django.conf import settings
from django.contrib.auth import logout as auth_logout
from app.models.customer import Customer

class LoginPage(View):

    template_name = "login.html"
    resaturant_dashboard="restaurant/restaurant-dashboard.html"

    def get(self, request):
        if request.user and request.user.is_authenticated:
            if (request.user.user_type == 1):
                return HttpResponse('admin dashboard')
            if (request.user.user_type == 2):
                return redirect('restaurant-dashboard')
            if (request.user.user_type == 3):
                return HttpResponse('delivery partner dashboard')
            if (request.user.user_type == 4):
                return redirect('user-dashboard')
        return render(request, self.template_name)


class LoginViewSet(APIView):
    """
         User Login
        :param value: email, password 
        :return
    """
    permission_classes = (AllowAny, )

    def post(self, request):
        username = request.data.get("email", None)
        password = request.data.get("password", None)

        if username is None or password is None:
            return error_response('Please provide both username and password.')
        user = authenticate(username=username, password=password)
        
        if not user:
            return error_response('The username is not a registered admin panel account.')
            
        if not user.is_active:
            return error_response('Please contact an administrator regarding this account.')

        login(request, user)
        customer=Customer.get_customer_by_user_id(user.id)
        print("saved",customer)
        if customer:
            request.session["customer_id"]=customer.id

        return success_response('Login Success: User logged in Successfully')

        
class LogoutViewSet(View):
    
    template_name = "login.html"

    def get(self, request):
        auth_logout(request)
        logout(request)
        return redirect(settings.LOGIN_URL)


class AdminViewset(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminProfileSerializer
    def create(self, request, *args, **kwargs):
        serializer = super().create(request, *args, **kwargs)
        return Response({"Success": "Registered Sucessfully"},)