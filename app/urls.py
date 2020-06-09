from django.urls import path,include
from app import views as app_views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'friends', app_views.FriendViewset)
router.register(r'belongings', app_views.BelongingViewset)
router.register(r'borrowings', app_views.BorrowedViewset)
router.register(r'users', app_views.UserViewset)

urlpatterns = [
    path('upload/', app_views.upload,name='upload'),
    path('list/', app_views.list,name='list'),
    path('', include(router.urls)),
]