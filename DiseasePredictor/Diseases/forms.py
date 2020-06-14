from django import forms
from . import models

class Symptom_Form(forms.ModelForm):

    class Meta:
        model = models.Symptom_List
        fields = '__all__'
        widgets = {
                'symptom1' : forms.TextInput(attrs = { 'class' : 'field' , 'hidden':True }),
                'symptom2' : forms.TextInput(attrs = { 'class' : 'field' , 'hidden':True }),
                'symptom3' : forms.TextInput(attrs = { 'class' : 'field' , 'hidden':True }),
                'symptom4' : forms.TextInput(attrs = { 'class' : 'field' , 'hidden':True }),
                'symptom5' : forms.TextInput(attrs = { 'class' : 'field' , 'hidden':True }),
                'symptom6' : forms.TextInput(attrs = { 'class' : 'field' , 'hidden':True }),
                'symptom7' : forms.TextInput(attrs = { 'class' : 'field' , 'hidden':True }),
                }
