from django import forms
from .models import Service,Quantity,Item
from django.contrib.auth.models import User


class ser_req(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
    
class buy(forms.ModelForm):     #new
    class Meta:                 #new
        model = Quantity               #new
        fields = '__all__'           #new
    

class item_form(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'