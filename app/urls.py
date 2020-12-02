from django.urls import path,include
from app.views.auth import *
from app.views.restaurant import *
from app.views.delivery import *
from app.views.user import *
from rest_framework import routers
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
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
    path('login/', LoginPage.as_view(), name='login-page'),
    path('login/api/', LoginViewSet.as_view(), name='login'),
    path('logout/', login_required(LogoutViewSet.as_view()), name='logout-page'),
    #User

    path('user-signup/', TemplateView.as_view(template_name='user-signup.html'), name='user-signup'),
    path('dashboard/', login_required(UserDashboardView.as_view()), name='user-dashboard'),
    path('user-orders/', login_required(UserOrdersView.as_view()), name='user-orders'),
    path('user-order-detail/<int:order_id>/', login_required(UserOrderDetailView.as_view()),
         name="user-order-detail"),

    #Restaurant
    path('restaurant-signup/', RestaurantView.as_view(), name='create-restaurant-profile'),
    path('restaurant-dashboard/', login_required(RestaurantDashaboard.as_view()), name='restaurant-dashboard'),
    path('restaurant-orders/', login_required(RestaurantOrders.as_view()), name='restaurant-orders'),
    path('restaurant-order-detail/<int:order_id>', login_required(RestaurantOrderDetail.as_view()), name='restaurant-order-detail'),

    path('restaurant/<int:restaurant_id>/', RestaurantMenuView.as_view(),
         name="view-restaurant-menu"),
    path('create-food-profile/', login_required(FoodItemView.as_view()), name='create-food-profile'),
    path('edit-food-profile/<int:food_id>', login_required(FoodItemView.as_view()), name='edit-food-profile'),
    path('add-to-cart/',login_required(AddtoCartViewSet.as_view()), name='add-to-cart'),
    path('get-cart/',login_required(GetCartViewSet.as_view()), name='get-cart'),
    path('cart/', login_required(CartView.as_view()), name='user-cart'),
    path('place-order/',login_required(PlaceOrderAPIView.as_view()), name='place-order'),
    path('foods/', login_required(FoodsView.as_view()), name='food-list'),
    path('upload-food-csv/', food_upload, name="food-upload"),
    path('export-food-csv/', food_export, name="food-export"),


    #Delivery Person
    path('dperson-signup/', DeliveryPersonView.as_view(), name='create-dperson-profile'),

    
    path('api/', include(router.urls)),
]