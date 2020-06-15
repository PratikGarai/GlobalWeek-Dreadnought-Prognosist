from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import forms
import requests
import json
import pickle
import os
from DiseasePredictor import settings

BASE_DIR = settings.BASE_DIR
symptoms = pickle.load(open(os.path.join(BASE_DIR, "media", "data", "all_ordered.p"), "rb")) 

def register(request):

    if request.method=="POST":

        registered = False
        
        user_form = forms.UserForm(data = request.POST)
        doctor_form = forms.Single_UserForm(data = request.POST)
        
        if user_form.is_valid() and doctor_form.is_valid():

            if validity(doctor_form.cleaned_data['official_name'], doctor_form.cleaned_data['mci_id'], doctor_form.cleaned_data['registration_year']):
                user = user_form.save()
                user.set_password(user.password)
                user.save()
            
                doctor = doctor_form.save(commit = False)
                doctor.user = user
                doctor.save()
                registered = True

                return render(request, "message.html", {'message': "You have successfully registered", 'header': "Registration Success"})
            return render(request, "message.html", {'message':"Your creditials did not match. Make sure you are registered in MCI", 'header': "Credentials Mismatch" })
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
                return render(request, "login.html", {'log' :forms.UserForm,  'message': "Your account is Inactive!"})
            return render(request, "login.html", {'log': forms.UserForm, 'message':'Wrong Credentials'})
        return render(request, "something_wrong.html",{}) 

    return render(request, "login.html", { 'log' : forms.UserForm , 'correct':1,  'message' : ""})

@login_required
def logout_user(request):
    logout(request)
    return render(request, "login.html", { 'log' : forms.UserForm, 'message': "You logged out"})


#AUXILLIARY METHODS
def validity(name , regno , year):
    url = 'https://mciindia.org/MCIRest/open/getPaginatedData?service=getPaginatedDoctor&draw=1&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=5&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=6&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=asc&start=0&length=500&search%5Bvalue%5D=&search%5Bregex%5D=false&name='+str(name)+'&registrationNo='+str(regno)+'&smcId=&year='+str(year)+'&_=1591867656238'
    response  = requests.get(url)
    vals = json.loads(response.content)
    l = len(vals['data'])
    if(l>0):
        return True
    return False

@login_required
def add_disease(request):
    if request.method =="POST":
        handle(request.POST)
    
    list_main = sorted(list(symptoms.keys()))
    l = len(list_main)
    return render(request, "data_adder.html", {'list_1':list_main[0::3] , 'list_2':list_main[1::3] ,'list_3':list_main[2::3] })

def handle(dictionary):
    pass 
