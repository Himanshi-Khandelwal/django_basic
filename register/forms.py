from django import forms
from django.contrib.auth.forms import UserCreationForm
from pagedown.widgets import PagedownWidget
from django.contrib.auth import get_user_model
from .models import images

User = get_user_model()

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
