from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from olx2.models import OlxCreate


class RegistrationForm(UserCreationForm):
     class Meta:
          model=User
          fields=["username","password1","password2","email"]

class LoginForm(forms.Form):
     username=forms.CharField()
     password=forms.CharField()

class OlxCreateForm(forms.ModelForm):
     class Meta:
          model=OlxCreate
          fields="__all__"

          


