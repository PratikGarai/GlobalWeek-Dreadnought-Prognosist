from django.db import models
from django.contrib.auth.models import User

class Single_User(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    official_name = models.CharField(max_length  = 256, help_text = "As it appears in MCI license")
    mci_id = models.CharField(max_length = 256)
    registration_year = models.PositiveSmallIntegerField(help_text="YYYY format")
