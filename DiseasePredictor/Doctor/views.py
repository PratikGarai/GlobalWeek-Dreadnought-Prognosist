from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
            return render(request, "message.html", {'message': "You have successfully registered", 'header': "Registration Success"})
        return render(request, "something_wrong.html",{}) 
    
    return render(request, "registration.html", {'User':forms.UserForm ,'Doctor':forms.Single_UserForm })


def login_user(request):
    
    if request.method=="POST":
        if True:
            username = request.POST.get('username')    
            password = request.POST.get('password')

            user = authenticate(username=username , password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return render(request, "message.html", {'message': "You have Successfully logged in!", 'header': "Login Succes"})
                return render(request, "message.html", {'message': "Your account is Inactive!", 'header': "Inactive"})
            return render(request, "login.html", {'log': forms.UserForm, 'Correct': False , 'message':''})
        return render(request, "something_wrong.html",{}) 

    return render(request, "login.html", { 'log' : forms.UserForm , 'Correct' : True, 'message' : "Fill the form to Login"})

@login_required
def logout_user(request):
    logout(request)
    return render(request, "login.html", { 'log' : forms.UserForm, 'Correct' : True, 'message': "You logged out"})
