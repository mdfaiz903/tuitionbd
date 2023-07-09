from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Contact,post
from .forms import post_form
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
#for showing post list
def post_detail(request,id):
    postdetail = post.objects.get(id=id)
    return render(request,'tuition/postdetail.html',{'postdetail':postdetail})
#for showing post list
def post_list_view(request):
    postlist = post.objects.all()
    return render(request,'tuition/postlist.html',{'postList':postlist})
def postview(request):
    P_data = post.objects.all()

    return render(request,'tuition/postview.html',{'post':P_data})




# def postcreate(request):
# 	# dictionary for initial data with
# 	# field names as keys
# 	context ={}

# 	# add the dictionary during initialization
# 	form = post_form(request.POST or None)
# 	if form.is_valid():
# 		form.save()
		
# 	context['form']= form
# 	return render(request, "tuition/post_create.html", context)

def postcreate(request):
    if request.method=='POST':
        form = post_form(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            #for multiselect_manytomany_fields
            sub = form.cleaned_data['subject']
            for i in sub:
                obj.subject.add(i)
                obj.save()
            cls = form.cleaned_data['class_in']
            for i in cls:
                obj.class_in.add(i)
                obj.save()
        return HttpResponseRedirect('/tuition/postview/')

    else:
        form = post_form()
    return render(request,'tuition/post_create.html',{'form':form})
#  Alternative code for postcreate function_class_Based   
# from django.views.generic import CreateView
# from django.urls import reverse_lazy
# class postCreateview(CreateView):
#     model=post
#     form_class=post_form
#     template_name='tuition/post_create.html'
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
#     def get_success_url(self):
#         return reverse_lazy('tuition:postview')

def about(request):
    return render(request,'about.html')