from django.shortcuts import render,redirect
from django import views
from django.views.generic import ListView,UpdateView,DeleteView,CreateView,FormView
from superAdmin.forms import VehiclesForm,RegistrationForm,LoginForm
from django.urls import reverse_lazy
from superAdmin.models import Vehicles,CustomUser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)    
    return wrapper

def superadminRequired(user):
    return user.is_authenticated and user.role in (1)

def adminOrSuperadminRequired(user):
    return user.is_authenticated and user.role in (1,2)

a=[signin_required,never_cache,user_passes_test(adminOrSuperadminRequired)]
b=[signin_required,never_cache,user_passes_test(superadminRequired)]
c=[signin_required,never_cache]

class SignUpView(CreateView):
    model=CustomUser
    form_class=RegistrationForm
    template_name: str="registration.html"
    success_url=reverse_lazy("signin")

    def form_valid(self, form):
        # messages.success(request,"REGISTRATION COMPLETED SUCCESSFULLY")
        return super().form_valid(form)

class LoginView(FormView):
    form_class=LoginForm
    template_name="login.html"

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password") 
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                # messages.success(request,"LOGIN COMPLETED SUCCESSFULLY")
                return redirect("home")
            else:
                # messages.error(request,"LOGIN FAILED")
                return render(request,self.template_name,{"form":form})

# class VehicleCreateView(views.View):
#    def get(self,request,*args,**kwargs):
#         form=VehiclesForm()
#         return render(request,"addVehicle.html",{"form":form})
    
#    def post(self,request,*args,**kwargs):
#         form=VehiclesForm(request.POST)
#         if form.is_valid():
#             # t_name=form.cleaned_data.get("task_name")
#             # usr=form.cleaned_data.get("user")
#             # Todos.objects.create(task_name=t_name,user=usr)
#             form.save()
#             return redirect("addvehicle")
#         else:
#             return render(request,"addVehicle.html",{"form":form})
@method_decorator(c,name="dispatch")      
class VehicleCreateView(CreateView):
    model=Vehicles
    template_name="addVehicle.html"
    form_class=VehiclesForm
    success_url=reverse_lazy("home")
    context_object_name="vehicle"

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
     
@method_decorator(c,name="dispatch")
class VehicleListView(ListView):
    model=Vehicles
    context_object_name="Vehicles"
    template_name="vehicleslist.html"

    def get_queryset(self):
        return Vehicles.objects.all() 
    
@method_decorator(a,name="dispatch")
class VehicleEditView(UpdateView):
    model=Vehicles
    form_class=VehiclesForm
    template_name="vehicleEdit.html"
    success_url=reverse_lazy("home")
    pk_url_kwarg="id"

@method_decorator(b,name="dispatch")
class VehicleDeleteView(views.View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Vehicles.objects.filter(id=id).delete()
        return redirect("home")

a   
def signOut(request,*args,**kwargs):
    logout(request)
    return redirect("signin")