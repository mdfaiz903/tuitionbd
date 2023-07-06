from django.contrib import admin
from . models import Contact,post,Class_in,Subject
# Register your models here.
admin.site.register(Contact)
admin.site.register(post)
admin.site.register(Subject)
admin.site.register(Class_in)