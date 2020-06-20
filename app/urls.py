from django.urls import path,include
from app.views.auth import *
from app.views.restaurant import *
from app.views.delivery import *
from rest_framework import routers
from django.views.generic import TemplateView
router = routers.DefaultRouter()
router.register(r'users/api',UserViewset)
router.register(r'restaurant/api',RestaurantViewset)
router.register(r'delivery/api',DeliveryPersonViewset)


urlpatterns = [
    path('login/', LoginPage.as_view(), name='login-page'),
    path('login/api/', LoginViewSet.as_view(), name='login'),
    path('user-signup/', TemplateView.as_view(template_name='user-signup.html'), name='user-signup'),
    
    #Restaurant
    path('restaurant-signup/', RestaurantView.as_view(), name='create-restaurant-profile'),
    
    path('', include(router.urls)),
]