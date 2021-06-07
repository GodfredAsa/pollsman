from django import forms
#from .models import Question
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name',)
        
        widgets = {
            'username': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Enter Category '}),
            
        }