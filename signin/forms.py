from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('flat_number', 'mobile_number','pro_pic')


        
class Editprofile(UserChangeForm):
    class Meta:
       
        model = User
        fields =('first_name','last_name','username','email')


