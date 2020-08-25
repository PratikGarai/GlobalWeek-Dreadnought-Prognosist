# GlobalWeek-Hackathon-Dreadnought

<h2> Prognosist </h2>
<hr>
A Django webapp to accept the symptoms of a user and present a probabilistic prognosis of diseases. This webapp also has a Doctor's login and registration through their MCI details to unlock the feauture of reporting new diseases and their related symtoms.  

<hr>
Our project for DeveloperWeek 2020 Global Hackathon

Packages to install (to be updated by collaborators who install something extra):<br>
1: Django<br>
2: Sklearn<br>
3: Argon2 and Argon2_cffi<br>
4: Requests<br>
5: Json<br>
6: Pickle<br>

-----------------------------------------------------------------------------------------
The dataset used : https://www.kaggle.com/rabisingh/symptom-checker

The dataset is located in : /Analysis/Training.csv

<hr>
<h2>An Important Note</h2>
People may encounter and error as shown in https://github.com/PratikGarai/GlobalWeek-Hackathon-Dreadnought/issues/2#issue-678986184<br><br>
This happen when the OS running the server has an architecture different from the OS architecture where the model was trained. For this reason, both 32bit and 64bit trained models have been added in the directory : <br>
<i>DiseasePredictor/media/models</i><br><br>

To use 32 bit models:<br> 
 Uncomment line number 42 and 45 of <i>DiseasePredictor/Diseases/views.py</i> and comment line numbers 43 and 46.<br>
To use 64 bit models:<br>
 Do vice-ersa of the steps of 32bit.
