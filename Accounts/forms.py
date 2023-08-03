from django import forms
from django.db.models import fields
from django.forms.models import ModelForm
from .models import AddBonus, Sale, User
from django.contrib.auth.forms import UserCreationForm

class Loginform(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
class SaleForm(ModelForm):
    class Meta:
        model=Sale
        fields=['sale']

class Addbonusform(ModelForm):
    class Meta:
        model=AddBonus
        fields=['employee','Bonus']


class Signup(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta :
        model= User
        fields=('username', 'email', 'password1', 'password2','is_employee','Age','Address','Salary')



   
