
from django.urls import path
from . views import homeview

urlpatterns = [
    
    path('home/', homeview, name= "home"),
]
