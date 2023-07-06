
from django.urls import path
from . views import homeview,contact,post,postview,postcreate

urlpatterns = [
    
    path('home/', homeview, name= "home"),
    path('contact/', contact, name= "contact"),
    path('post/', post, name= "post"),
    path('postview/', postview, name= "postview"),
    path('postcreate/', postcreate, name= "postcreate"),
]
