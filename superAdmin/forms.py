from django import forms
from superAdmin.models import Vehicles,CustomUser
from django.contrib.auth.forms import UserCreationForm
class RegistrationForm(UserCreationForm):

    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}),label="PASSWORD1")
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}),label="PASSWORD2")

    class Meta:
        model=CustomUser
        fields=[
            "username",
            "email",
            "role"
        ]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "role":forms.Select(attrs={"class":"form-select form-control"})
        }
        labels={

            "username":"USERNAME",
            "email":"EMAIL",
            "role":"ROLE",
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),label="USERNAME")
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}),label="PASSWORD")


class VehiclesForm(forms.ModelForm):
    class Meta:
        model=Vehicles
        fields=["v_number","v_type","v_model","v_description"]
        widgets={
            "v_number":forms.TextInput(attrs={"class":"form-control"}),
            "v_type":forms.Select(attrs={"class":"form-control"}),
            "v_model":forms.TextInput(attrs={"class":"form-control"}),
            "v_description":forms.TextInput(attrs={"class":"form-control"}),

         }
        labels={
            "v_number":"VEHICLE NUMBER",
            "v_type":"VEHICLE TYPE",
            "v_model":"VEHICLE MODEL",
            "v_description":"VEHICLE DESCRIPTION",
         }