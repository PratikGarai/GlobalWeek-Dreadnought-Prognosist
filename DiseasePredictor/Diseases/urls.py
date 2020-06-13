from django.urls import path
from django.conf.urls import url
from . import views

app_name = "Diseases"

urlpatterns = [
        path("input/", views.input_view, name="Input"),
        ]
