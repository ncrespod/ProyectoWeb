from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View 
from django.http import HttpResponse, JsonResponse
from datetime import datetime
import random

# Importo Firebase Admin SDK 
import firebase_admin

# Definimos las credenciales que nos permitirán usar Firebase Admin SDK 
from firebase_admin import credentials

# Importo el Servicio Firebase Realtime Database 
from firebase_admin import db

class Reg2(View):

	# Especifico la plantilla o template que usaré 
	template_name = "tables-simple2.html"

	# Llamo al archivo JSON que contiene mi clave privada 


	
	# Envio los datos de la tabla 'alertas' a la vista o template 
	def get(self, request):	
		
		if request.method == "GET":
            
			# Accedo a la base de datos, específicamente a la tabla 'alertas' 
			ref = db.reference('Tempera')
			print(ref.get())
			task=request.POST.get('task')
			print(task)
			# Llamo los datos que se encuentran en la tabla 'alertas' 
			datos = ref.get()
			return render(request, self.template_name, { "data3": datos})