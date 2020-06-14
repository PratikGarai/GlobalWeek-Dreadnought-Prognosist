from django.shortcuts import render
from . import forms

symptoms_list = ['symptom1','symptom2','symptom3','symptom4' ]
def input_view(request):

    if request.method=="POST":

        symptoms_form = forms.Symptom_Form(data = request.POST)
        if symptoms_form.is_valid():
            ml(symptoms_form.cleaned_data)
            return render(request, "message.html", {'message': "Everything took place as planned!", 'header': "Form Success"})
        
        return render(request, "something_wrong.html", {})
    
    return render(request, "input.html",{'form': forms.Symptom_Form, 'symptoms': symptoms_list})

def ml(clean_data):
    print(clean_data)
