from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from BikeKart.models import Vehicle

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()


class VehicleAddForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields=[
            "name",
            "owner",
            "brand_object",
            "year",
            "km_driven",
            "description",
            "category",
            "image",
            "location",
            "owner_types",
            "price"
        ]
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'owner':forms.TextInput(attrs={'class':'form-control'}),
            'year':forms.NumberInput(attrs={'class':'form-control'}),
            'km_driven':forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'category':forms.TextInput(attrs={'class':'form-control'}),
            # 'image':forms.TextInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'owner_types':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
        }


