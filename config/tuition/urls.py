
from django.urls import path
from . views import contact,post,postview,postcreate,about,post_list_view,postDelete,post_detail,postEdit,searchview

urlpatterns = [
    
    
    path('contact/', contact, name= "contact"),
    path('post/', post, name= "post"),
    path('postview/', postview, name= "postview"),
    path('postlist/', post_list_view, name= "postlist"),
    path('post_detail/<int:id>/', post_detail, name= "post_detail"),
    path('postcreate/', postcreate, name= "postcreate"),
    path('postEdit/<int:pk>/', postEdit.as_view(), name= "postEdit"),
    
    path('postDelete/<int:pk>/', postDelete.as_view(), name= "postDelete"),
    path('search', searchview.as_view(), name= "search"), #search urls
    path('about_us/', about, name= "about_us"),
]
