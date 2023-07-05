from django.shortcuts import render
from .models import Contact,post
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

def postview(request):
    P_data = post.objects.all()

    return render(request,'tuition/postview.html',{'post':P_data})