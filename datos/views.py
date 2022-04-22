from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View 
from django.http import HttpResponse, JsonResponse
import csv 
import pandas as pd
from firebase_admin import db

class ReportePersonalizadoExcel(TemplateView):
    def get(self,request,*args,**kwargs):
        ref = db.reference('Suel') 
        queryset = ref.get()
        a = list(queryset)
        field_names = ['id','HoraFecha', 'h2'] 
        data = [] 

        for i in a:
            if i:
                data.append(i)
        
        
        with open('Names.csv', 'w') as csvfile: 
            writer = csv.DictWriter(csvfile, fieldnames = field_names) 
            writer.writeheader() 
            writer.writerows(data) 
    
        nombre_archivo = "ReporteHumedadSuelo.xlsx"
        response = HttpResponse(content_type = "application/ms-excel")
        contenido = "attachment; filename = {0}".format(nombre_archivo)
        response["Content-Disposition"] = contenido
        df = pd.read_csv('Names.csv')
        df.to_excel(response, index=False)
        return response
