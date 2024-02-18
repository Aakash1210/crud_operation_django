from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NetworkAdminViewSet, RouterViewSet

router = DefaultRouter()
router.register(r'network-admin', NetworkAdminViewSet)
router.register(r'router', RouterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
