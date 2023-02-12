from django.contrib import admin
from django.urls import path
from home import views
from django.urls import path, include
 

# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('', views.home,name='home'),
    path('',views.about,name='about')
    
]