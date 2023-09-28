from django import forms
from olxapp.models import Olx
from django.contrib.auth.models import User
class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "phone":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
        }
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    







class OlxCreateForm(forms.ModelForm):
    class Meta:
        model=Olx
        fields="__all__"
        widgets={'name':forms.TextInput(attrs={"class":"form-control"}),
                 "company":forms.TextInput(attrs={"class":"form-control"}),
                 "number":forms.TextInput(attrs={"class":"form-control"}),
                "price":forms.NumberInput(attrs={"class":"form-control"}),
                "phone":forms.NumberInput(attrs={"class":"form-control"}),
                


                 
                 

        }
