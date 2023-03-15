from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text="Enter your first name")
    last_name = forms.CharField(max_length=100, help_text="Enter your last name")
    email = forms.EmailField(help_text="Enter your Email")
    password = forms.CharField(label="Set password",widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password",widget= forms.PasswordInput)
        
    class Meta:
        model= User
        fields = ['first_name','last_name','username','password','password2']
        help_texts = {
            'username':None,
            'password':None
        }