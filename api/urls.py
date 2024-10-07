# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserGroupViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', UserGroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
