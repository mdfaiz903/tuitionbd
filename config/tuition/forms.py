from django import forms 
from.models import post

class post_form(forms.ModelForm):
    class Meta:
        model=post
        exclude= ['user','slug','id','created_at']
        widgets={
            'class_in':forms.CheckboxSelectMultiple(attrs={'multiple':True}),
            'subject':forms.CheckboxSelectMultiple(attrs={'multiple':True}),
        }