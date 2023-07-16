from django.urls import path
from . views import loginuser,logoutuser,registation

urlpatterns = [
    
    
    path('login/', loginuser, name= "login"),
    path('logout/', logoutuser, name= "logout"),
    path('registation/', registation, name= "registation"),
 
]
