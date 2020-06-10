from django.shortcuts import render
from . import forms

def register(request):

    if request.method=="POST":

        registered = False
        
        user_form = forms.UserForm(data = request.POST)
        doctor_form = forms.Single_UserForm(data = request.POST)
        
        if user_form.is_valid() and doctor_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            doctor = doctor_form.save(commit = False)
            doctor.user = user

            print(doctor_form)

            # commented for now, some validity checker here
            # if validity(doctor_form):
            #     doctor.save()
            #     registered = True
            #     return render(request, "registration_success.html", {})
            # for now, I make registered true for testing
            doctor.save()
            registered = True
            return render(request, "registration_success.html", {})
        return render(request, "something_wrong.html",{}) 

    else:
        return render(request, "registration.html", {'User':forms.UserForm ,'Doctor':forms.Single_UserForm })
