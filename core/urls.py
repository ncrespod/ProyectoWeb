# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from alertas.views import Alertas
from registros.views import Reg

urlpatterns = [

    path('admin/', admin.site.urls),          # Django admin route
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls")), 
    path('',include('com.urls',namespace='com')),
    path('',include("registros.urls")),
    
    
 
  
    
   
   
               # UI Kits Html files
]
