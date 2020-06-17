from django.urls import path,include
from .views import *
from rest_framework import routers
from django.views.generic import TemplateView
router = routers.DefaultRouter()
router.register(r'friends', FriendViewset)
router.register(r'belongings',BelongingViewset)
router.register(r'borrowings', BorrowedViewset)
router.register(r'users',UserViewset)


urlpatterns = [
    path('login/', LoginPage.as_view(), name='login-page'),
    path('login/api/', LoginViewSet.as_view(), name='login'),
    path('user-signup/', TemplateView.as_view(template_name='user-signup.html'), name='user-signup'),
    path('upload/', upload,name='upload'),
    path('list/', display,name='list'),
    path('', include(router.urls)),
]