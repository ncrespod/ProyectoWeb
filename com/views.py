from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View 
from django.http import HttpResponse, JsonResponse
from datetime import datetime, timezone
import pytz
import random
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def fetch_sensor_values_ajax(request):
    data={}
    if request.is_ajax():
        sensor_data=[]
        now=datetime.now(pytz.timezone('America/Bogota'))
        ok_date=str(now.strftime('%Y-%m-%d %H:%M:%S'))
        ref = db.reference('Data/id/suelo')
        sensor_val=ref.get()   
        sensor_data.append(str(sensor_val)+','+ok_date)
        print(sensor_data)
        data['result']=sensor_data
    else:
        data['result']='Not Ajax'
    return JsonResponse(data)

def fetch_sensor_values_ajax2(request):
    data={}
    if request.is_ajax():
        sensor_data=[]
        now=datetime.now(pytz.timezone('America/Bogota'))
        ok_date=str(now.strftime('%Y-%m-%d %H:%M:%S'))
        ref = db.reference('Data/id/Temperatura') 
        print(ref.get())
        sensor_val=ref.get()   
        sensor_data.append(str(sensor_val)+','+ok_date)
        data['result']=sensor_data
    else:
        data['result']='Not Ajax'
    return JsonResponse(data)

def fetch_sensor_values_ajax3(request):
    data={}
    if request.is_ajax():
        sensor_data=[]
        now=datetime.now(pytz.timezone('America/Bogota'))
        ok_date=str(now.strftime('%Y-%m-%d %H:%M:%S'))
        ref = db.reference('Data/id/Humedad') 
        print(ref.get())
        sensor_val=ref.get()   
        sensor_data.append(str(sensor_val)+','+ok_date)
        data['result']=sensor_data
    else:
        data['result']='Not Ajax'
    return JsonResponse(data)

def fetch_sensor_values_ajax4(request):
    data={}
    if request.is_ajax():
        sensor_data=[]
        now=datetime.now(pytz.timezone('America/Bogota'))
        ok_date=str(now.strftime('%Y-%m-%d %H:%M:%S'))
        ref = db.reference('Data/id/LDR') 
        print(ref.get())
        sensor_val=ref.get()   
        sensor_data.append(str(sensor_val)+','+ok_date)
        data['result']=sensor_data
    else:
        data['result']='Not Ajax'
    return JsonResponse(data)

