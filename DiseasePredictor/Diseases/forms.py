from django import forms
from . import models

class Symptom_Form(forms.ModelForm):

    class Meta:
        model = models.Symptom_List
        fields = '__all__'
        widgets = {
                'symptom1' : forms.TextInput(attrs = { 'class' : 'field' , 'readonly':True }),
                'symptom2' : forms.TextInput(attrs = { 'class' : 'field' , 'readonly':True }),
                'symptom3' : forms.TextInput(attrs = { 'class' : 'field' , 'readonly':True }),
                'symptom4' : forms.TextInput(attrs = { 'class' : 'field' , 'readonly':True }),
                'symptom5' : forms.TextInput(attrs = { 'class' : 'field' , 'readonly':True }),
                'symptom6' : forms.TextInput(attrs = { 'class' : 'field' , 'readonly':True }),
                'symptom7' : forms.TextInput(attrs = { 'class' : 'field' , 'readonly':True }),
                }
