# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from cgitb import html
from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from alertas.views import Postres
from django.conf.urls.static import static 

urlpatterns = [
   
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("alertas/", Postres.as_view(), name="tables-data"),
   
    
    
]
