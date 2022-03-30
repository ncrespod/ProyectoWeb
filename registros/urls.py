from webbrowser import get
from django.urls import path
from .views import *


urlpatterns = [ 
    path('', get, name="get"),

]