
from django.urls import path
from . views import homeview,contact,post

urlpatterns = [
    
    path('home/', homeview, name= "home"),
    path('contact/', contact, name= "contact"),
    path('post/', post, name= "post"),
]
