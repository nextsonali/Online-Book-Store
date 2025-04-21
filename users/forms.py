from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
    
        labels = {
                'username' : 'Username',
                'password' : 'Password',
        }

        widgets  = {
                'username' : forms.TextInput(attrs={'placeholder': 'eg. UserName'}),
                'password' : forms.TextInput(attrs={'placeholder': 'eg. Password'}),
        }

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    
