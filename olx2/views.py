from olx2.forms import RegistrationForm,LoginForm,OlxCreateForm
from django.views.generic import View,CreateView,ListView,UpdateView
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from olx2.models import OlxCreate
from django.utils.decorators import method_decorator

def signin_dec(fn):
     def wrapper(request,*args,**kwargs):
          if not request.user.is_authenticated:
               return redirect("signin")
          else:
               return fn(request,*args,**kwargs)
     return wrapper




class SignUpView(View):
     def get(self,request,*args,**kwargs):
          form=RegistrationForm()
          return render(request,"olx2/sign_up.html",{"form":form})
     def post(self,request,*args,**kwargs):
          form=RegistrationForm(request.POST)
          if form.is_valid():
               form.save()
               messages.success(request,"Registration completed")

               return render(request,"olx2/sign_up.html",{"form":form})
          else:
               messages.error(request,"Registration failed")
               return render(request,"olx2/sign_up.html",{"form":form})
          

class SignInView(View):
     def get(self,request,*args,**kwargs):
          form=LoginForm()
          return render(request,"olx2/signin.html",{"form":form})
     def post(self,request,*args,**kwargs):
          form=LoginForm(request.POST)
          if form.is_valid():
               uname=form.cleaned_data.get("username")
               pwd=form.cleaned_data.get("password")
               usr=authenticate(request,username=uname,password=pwd)
               if usr:
                    login(request,usr)
                    messages.success(request,"login succesfully")
                    return redirect("signin")
               else:
                    messages.error(request,"login failed")
                    return redirect("signup")
               
@method_decorator(signin_dec,name="dispatch")
class OlxCreateView(CreateView):
     template_name="olx2/add.html"
     form_class=OlxCreateForm
     success_url=reverse_lazy("olx-add")


@method_decorator(signin_dec,name="dispatch")
class OlxListView(ListView):
     template_name="olx2/list.html"
     model=OlxCreate
     context_object_name="vehicles"
     def get_queryset(self): #  it used to list the todos of the signed in person only
        qs=OlxCreate.objects.filter(user=self.request.user)
        return qs

     
@method_decorator(signin_dec,name="dispatch")
class OlxUpdateView(UpdateView):
     template_name="olx2/list.html"
     model=OlxCreate
     form_class=OlxCreateForm
     success_url=reverse_lazy("olx-list")

@signin_dec
def remove_todo(request,*args,**kwargs):
    id=kwargs.get("pk")
    OlxCreate.objects.filter(id=id).delete()
    return redirect("olx-list")