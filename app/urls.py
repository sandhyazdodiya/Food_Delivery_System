from django.urls import path,include
from app.views.auth import *
from app.views.restaurant import *
from app.views.delivery import *
from app.views.user import *
from rest_framework import routers
from django.views.generic import TemplateView
router = routers.DefaultRouter()



#Restaurant
router.register(r'restaurant',RestaurantViewset)    #Register Restaurant 
router.register(r'fooditem',FoodItemViewset)
router.register(r'order',OrderViewset)
router.register(r'orderitem',OrderItemViewset)

#Register DeliveryPerson
router.register(r'delivery',DeliveryPersonViewset)

#Register Customer
router.register(r'customer',CustomerViewset)

#Register Admin
router.register(r'admin',AdminViewset)

urlpatterns = [
    path('', LoginPage.as_view(), name='login-page'),
    path('login/api/', LoginViewSet.as_view(), name='login'),
    path('logout/', LogoutViewSet.as_view(), name='logout-page'),
    #User
    path('user-signup/', TemplateView.as_view(template_name='user-signup.html'), name='user-signup'),
    path('dashboard/', UserDashboardView.as_view(), name='user-dashboard'),
    path('myorders/', UserOrdersView.as_view(), name='user-orders'),
    #Restaurant
    path('restaurant-signup/', RestaurantView.as_view(), name='create-restaurant-profile'),
    path('restaurant-dashboard/', RestaurantDashaboard.as_view(), name='restaurant-dashboard'),
    path('restaurant-orders/', RestaurantOrders.as_view(), name='restaurant-orders'),

    path('restaurant/<int:restaurant_id>/', RestaurantMenuView.as_view(),
         name="view-restaurant-menu"),
    path('create-food-profile/', FoodItemView.as_view(), name='create-food-profile'),
    path('edit-food-profile/<int:food_id>', FoodItemView.as_view(), name='edit-food-profile'),
    path('add_to_cart/',AddtoCartViewSet.as_view(), name='add-to-cart'),
    
    path('api/', include(router.urls)),
]