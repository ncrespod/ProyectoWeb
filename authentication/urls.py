# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from cgitb import html
from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from alertas.views import Alertas
from registros.views import Reg
from registros2.views import Reg2
from registros3.views import Reg3
from registros4.views import Reg4
from registros import views
from registros2 import views
from registros3 import views
from registros4 import views
from com import views
from django.conf.urls.static import static 

urlpatterns = [
   
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("alertas/", Alertas.as_view(), name="tables-data"),
    path("Registros/", Reg.as_view(), name="tables-simple"),
    path("Registros2/", Reg2.as_view(), name="tables-simple2"),
    path("Registros3/", Reg3.as_view(), name="tables-simple3"),
     path("Registros4/", Reg4.as_view(), name="tables-simple4"),
    path('fetch_sensor_values_ajax', views.fetch_sensor_values_ajax, name='fetch_sensor_values_ajax'),
    path('fetch_sensor_values_ajax2', views.fetch_sensor_values_ajax2, name='fetch_sensor_values_ajax2'),
    path('fetch_sensor_values_ajax3', views.fetch_sensor_values_ajax3, name='fetch_sensor_values_ajax3'),
    path('fetch_sensor_values_ajax4', views.fetch_sensor_values_ajax4, name='fetch_sensor_values_ajax4'),
    
]
