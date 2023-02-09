from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    type_choices = (
        (1, 'Super Admin'),
        (2, 'Admin'),
        (3, 'User'),
    )
    role = models.PositiveSmallIntegerField(choices=type_choices,default=3)

class Vehicles(models.Model):
    vehicle_types=(
    ('Two wheeler','Two wheeler'),
    ('Three wheeler','Three wheeler'),
    ('Four wheeler','Four wheeler'),
    )

    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="myuser")
    v_number=models.CharField(max_length=100)
    v_type=models.CharField(choices=vehicle_types,default="Two wheeler",max_length=100)
    v_model=models.CharField(max_length=100)
    v_description=models.TextField(max_length=200)

