from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


from BikeKart.forms import RegistrationForm,LoginForm,VehicleAddForm
from BikeKart.models import Vehicle


# SignUp View
# url : localhost:8000/register
# method : get, post
class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        return render(request,"register.html",{"form":form})


class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"signin.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_object=authenticate(request,username=u_name,password=pwd)
            if user_object:
                login(request,user_object)
                messages.success(request,"user logged in")
                return redirect("bikes-all")
        messages.error(request,"invalid credential!")
        return render(request,"signin.html",{"form":form}) 


# Vehicle list view 
# url: localhost:8000/vehicles/all/
# method: get
class VehicleListView(View):      
    def get(self,request,*args,**kwargs):
        qs=Vehicle.objects.all()
        return render(request,"index.html",{"data":qs})

# Vehicle list view 
# url: localhost:8000/vehicles/add/
# method: get, post
class VehicleAddView(View): 
    def get(self,request,*args,**kwargs):
        form=VehicleAddForm()
        return render(request,"vehicles_add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=VehicleAddForm(request.POST,files=request.FILES)
        if form.is_valid():
            data=form.cleaned_data
            Vehicle.objects.create(**data)
            messages.success(request,"Vehicle added successfully")
            return redirect("bikes-all")
        else:
            messages.error(request,"Failed to add vehicle")
            return render(request,"vehicles_add.html",{"form":form})


# Vehicle list view 
# url: localhost:8000/vehicles/{id}/
# method: get
class VehicleDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Vehicle.objects.get(id=id)
        return render(request,"vehicle_detail.html",{"data":qs})
   

class HomeView(TemplateView):
    template_name="base.html"