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
def list(request):
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