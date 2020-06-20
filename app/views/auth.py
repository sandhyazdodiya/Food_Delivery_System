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


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        serializer = super().create(request, *args, **kwargs)
        return Response({"Success": "Registered Sucessfully"},)

class LoginPage(View):
    template_name = "login.html"
    def get(self, request):
        if request.user and request.user.is_authenticated:
            return HttpResponse("success")
        return render(request, self.template_name)
class LoginViewSet(APIView):
    """
        User Login
        :param value: username, password -- Username will be email or username
        :return: user's email, token
    """
    permission_classes = (AllowAny, )

    def post(self, request):
        username = request.data.get("email", None)
        password = request.data.get("password", None)

        if username is None or password is None:
            return HttpResponse('Please provide both username and password.')
        user = authenticate(username=username, password=password)

        if not user:
            return HttpResponse('The username is not a registered admin panel account.')
            
        if not user.is_active:
            return HttpResponse('Please contact an administrator regarding this account.')

        login(request, user)
        return HttpResponse('Login Success: User logged in Successfully')
