from django.shortcuts import render,redirect
from olx.forms import OlxCreateForm,RegistrationForm,LoginForm
from django.views.generic import View
from  olxapp.models import Olx
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def sign_outview(request,*args,**kwargs):
    logout(request)
    return redirect("login")


class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            # form.save() we can see the password
            User.objects.create_user(**form.cleaned_data) #for hiding the password
            return redirect("login")
        else:
            return render(request,"login.html",{"form":form})

class SignInView(View):
        def get(self,request,*args,**kwargs):
             form=LoginForm()
             return render(request,"login.html",{"form":form})
        def post(self,request,*args,**kwargs):
             form=LoginForm(request.POST)
             if form.is_valid():
            # form.save() we can see the password
              uname=form.cleaned_data.get("username") #for hiding the password
              pwd=form.cleaned_data.get("password")
              usr=authenticate(request,username=uname,password=pwd)
              if usr:
                  login(request,usr)
                  messages.success(request,"login successfully")
                  print("credentilas are valid")
                  return redirect("olx-add")
              else:
                  print("invalid credentilas")
                  messages.error(request,"failed")
                  return render(request,"registration.html",{"form":form})





    
     


class OlxCreateView(View):
    def get(self,request,*args,**kwargs):
        form=OlxCreateForm()
        return render(request,"olx_add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=OlxCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print("save")
            return redirect("olx-list")
            
        else:
            return render(request,"olx_add.html",{"form":form})

class OlxListView(View):
    def get(self,request,*args,**kwargs):
        qs=Olx.objects.all()
        return render(request,"olx_list.html",{"vehicles":qs})

class OlxDetailView(View):
        def get(self,request,*args,**kwargs):
            id=kwargs.get("pk")
            qs=Olx.objects.get(id=id)
            return render(request,"olx_detail.html",{"vehicles":qs})
        
class OlxUpdateView(View):
        def get(self,request,*args,**kwargs):
            id=kwargs.get("pk")
            obj=Olx.objects.get(id=id)
            form=OlxCreateForm(instance=obj)
            return render(request,"olx_update.html",{"form":form})
        def post(self,request,*args,**kwargs):
            id=kwargs.get("pk")
            obj=Olx.objects.get(id=id)
            form=OlxCreateForm(request.POST,instance=obj,files=request.FILES)
            if form.is_valid():
                form.save()
                return redirect("olx-list")
            else:
                return render(request,"student_edit.html",{"form":form})


class OlxDeleteView(View):
    def get(self,request,*args,**kwrags):
        id=kwrags.get("pk")
        Olx.objects.filter(id=id).delete()
        return redirect("olx-list")

     
       


    
