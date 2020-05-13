from .views import signup,login,logout
from django.urls import path

urlpatterns = [
    path('signup/', signup, name = "signup"),
    path('login/', login, name = "login"),
    path('logout/', logout, name = "logout"),
    
]