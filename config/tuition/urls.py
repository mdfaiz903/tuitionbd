
from django.urls import path
from . views import homeview,contact,post,postview,postcreate,about,post_list_view

urlpatterns = [
    
    path('home/', homeview, name= "home"),
    path('contact/', contact, name= "contact"),
    path('post/', post, name= "post"),
    path('postview/', postview, name= "postview"),
    path('postlist/', post_list_view, name= "postlist"),
    path('postcreate/', postcreate, name= "postcreate"),
    path('about_us/', about, name= "about_us"),
]
