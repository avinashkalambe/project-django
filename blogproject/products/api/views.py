from django.contrib.auth.models import User
from products.models import Product
from .serializers import UserSerializer,ProductSerializer
from rest_framework import viewsets
from rest_framework import permissions

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


