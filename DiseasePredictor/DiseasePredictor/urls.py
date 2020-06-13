from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page),
    url('^Doctor/', include('Doctor.urls', namespace = 'Doctor')),
    url('^Diseases/', include('Diseases.urls', namespace = 'Diseases')),
]
