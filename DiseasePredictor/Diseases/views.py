from django.shortcuts import render
from . import forms
import pickle
from DiseasePredictor import settings
import os

BASE_DIR = settings.BASE_DIR
common = pickle.load(open(os.path.join(BASE_DIR,'media','data','common.p'), "rb"))
uncommon = pickle.load(open(os.path.join(BASE_DIR,'media','data','uncommon.p'), "rb"))
all_ordered = pickle.load(open(os.path.join(BASE_DIR,'media','data','all_ordered.p'), "rb"))

def input_view(request):

    if request.method=="POST":

        symptoms_form = forms.Symptom_Form(data = request.POST)
        if symptoms_form.is_valid():
            disease_prediction = ml(symptoms_form.cleaned_data)
            print(symptoms_form.cleaned_data)
            if len(disease_prediction)==1:
                return render(request, "result.html", {'multiple': 0, 'prognosis': disease_prediction[0][0]})
            else:
                return render(request, "result.html", {'multiple': 1, 'prognosis': disease_prediction})
        
        return render(request, "something_wrong.html", {'message' : "Something went wrong!"})
    
    return render(request, "input.html",{'form': forms.Symptom_Form, 'common': common,'uncommon':uncommon, 'length':7})




def ml(clean_data):
    values_1 = [ i for i in clean_data.values() ]
    l = [ all_ordered[i] for i in values_1 if i!='' ]
    
    test_list = [ 0 for i in range(132) ]
    for i in l :
        test_list[i] = 1
    
    model = None
    label_coder = None
    # with open('media/models/model_rf.sav', 'rb') as fp:
    with open('media/models/model_rf_64.sav', 'rb') as fp:
        model = pickle.load(fp)
    # with open('media/models/label_coder.sav', 'rb') as fp:
    with open('media/models/label_coder_64.sav', 'rb') as fp:
        label_coder = pickle.load(fp)
    ls = []
    threshold = 15

    result = model.predict_proba([test_list])
    for i in range(0,len(result[0])):
        if result[0][i]!=0:
            ls.append((label_coder.inverse_transform([i,]),(result[0][i]*100)))

    ls = sorted([ (i[0][0],int(i[1])) for i in ls if i[1]>=threshold ] , reverse=True, key=lambda x: x[1])
    if ls[0][1]<threshold:
        return ls[0]
    else:
        return ls
