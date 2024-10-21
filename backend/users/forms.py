from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class customuserCreationFrom(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['username','email','phone_number','address']