from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users',views.UserViewSet)
router.register('products',views.ProductViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('auth-api/',include('rest_framework.urls'),name= 'rest_framework')
    ]