from django import forms
from django.contrib.auth.models import User
from . import models

class Single_UserForm(forms.ModelForm):
    
    class Meta():
        model = models.Single_User
        fields = ('official_name','mci_id','registration_year')
    

class UserForm(forms.ModelForm):

    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password','email')
