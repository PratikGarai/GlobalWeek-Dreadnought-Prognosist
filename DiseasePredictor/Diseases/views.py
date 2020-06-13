from django.shortcuts import render
from . import forms

def input_view(request):

    if request.method=="POST":
        return None
    
    return render(request, "input.html",{'form': forms.Symptom_Form})
