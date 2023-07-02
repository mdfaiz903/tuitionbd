from django.shortcuts import render
from .models import *
# Create your views here.
def homeview(request):
    return render(request,'home.html')


def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        phone = request.POST['phone']
        content = request.POST['content']
        data = Contact(name=name,phone=phone,content=content)
        data.save()
    
    return render(request,'contact.html')