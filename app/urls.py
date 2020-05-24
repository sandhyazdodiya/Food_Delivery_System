from django.urls import path
from app import views
urlpatterns = [
    path('upload/', views.upload,name='upload'),
    path('list/', views.list,name='list'),
]