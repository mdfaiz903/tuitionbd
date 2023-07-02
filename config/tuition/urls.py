
from django.urls import path
from . views import homeview,contact

urlpatterns = [
    
    path('home/', homeview, name= "home"),
    path('contact/', contact, name= "contact"),
]
