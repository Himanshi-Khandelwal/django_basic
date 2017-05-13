from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pagedown.widgets import PagedownWidget
from .models import images

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class Form(forms.ModelForm):
    content=forms.CharField(widget=PagedownWidget)

    class Meta:
        model = images
        fields = [
            "title",
            "content",
            "image",
            


        ]
