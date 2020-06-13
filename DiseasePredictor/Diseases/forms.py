from django import forms
from . import models

class Symptom_Form(forms.ModelForm):

    class Meta:
        model = models.Symptom_List
        fields = '__all__'
