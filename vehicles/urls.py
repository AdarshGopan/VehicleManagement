"""vehicles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from superAdmin.views import VehicleCreateView,VehicleListView,LoginView,SignUpView,VehicleDeleteView,VehicleEditView,signOut
urlpatterns = [
    path('admin/', admin.site.urls),
    path('addvehicle/',VehicleCreateView.as_view(),name="addvehicle"),
    path('vehiclelist/',VehicleListView.as_view(),name="home"),
    path('vehicle/register',SignUpView.as_view(),name="signup"),
    path('vehicle/login',LoginView.as_view(),name="signin"),
    path('vehicle/update/<int:id>',VehicleEditView.as_view(),name="update"),
    path('vehicle/delete/<int:id>',VehicleDeleteView.as_view(),name="delete"),
    path('vehicle/logout',signOut,name="signout")




]
