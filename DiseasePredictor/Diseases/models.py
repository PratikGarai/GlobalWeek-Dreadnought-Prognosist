from django.db import models

class Symptom_List(models.Model):

    symptom1 = models.CharField(max_length=256 , blank = True)
    symptom2 = models.CharField(max_length=256 , blank = True)
    symptom3 = models.CharField(max_length=256 , blank = True)
    symptom4 = models.CharField(max_length=256 , blank = True)
    symptom5 = models.CharField(max_length=256 , blank = True)
    symptom6 = models.CharField(max_length=256 , blank = True)
    symptom7 = models.CharField(max_length=256 , blank = True)
