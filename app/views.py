from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from cloudinary.forms import cl_init_js_callbacks      
from .models import Photo,Friend,Borrowed,Belonging
from .forms import PhotoForm
import six
from rest_framework import viewsets
from .serializers import FriendSerializer,BelongingSerializer,BorrowedSerializer
from custom_user.serializers import UserSerializer
from custom_user.models import *
from custom_user.serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import status
from django.views import View
def filter_nones(d):
    return dict((k, v) for k, v in six.iteritems(d) if v is not None)
def upload(request):
  context = dict( backend_form = PhotoForm())

  if request.method == 'POST':
    form = PhotoForm(request.POST, request.FILES)
    context['posted'] = form.instance
    if form.is_valid():
        form.save()

  return render(request, 'upload.html', context)
def display(request):
    defaults = dict(format="jpg", height=150, width=150)
    defaults["class"] = "thumbnail inline"

    # The different transformations to present
    samples = [
        dict(crop="fill", radius=10),
        dict(crop="scale"),
        dict(crop="fit", format="png"),
        dict(crop="thumb", gravity="face"),
        dict(format="png", angle=20, height=None, width=None, transformation=[
            dict(crop="fill", gravity="north", width=150, height=150, effect="sepia"),
        ]),
    ]
    samples = [filter_nones(dict(defaults, **sample)) for sample in samples]
    return render(request, 'list.html', dict(photos=Photo.objects.all(), samples=samples))

class FriendViewset(viewsets.ModelViewSet):
    queryset =Friend.objects.all()
    serializer_class = FriendSerializer

class BelongingViewset(viewsets.ModelViewSet):
    queryset =Belonging.objects.all()
    serializer_class = BelongingSerializer

class BorrowedViewset(viewsets.ModelViewSet):
    queryset = Borrowed.objects.all()
    serializer_class = BorrowedSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        serializer = super().create(request, *args, **kwargs)
        return Response({"Success": "Registered Sucessfully"},)
class LoginPage(View):
    template_name = "login.html"
    def get(self, request):
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
