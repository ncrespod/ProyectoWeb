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
import json
class Reg(View):

	# Especifico la plantilla o template que usaré 
	template_name = "tables-simple.html"

	# Llamo al archivo JSON que contiene mi clave privada 


	
	# Envio los datos de la tabla 'alertas' a la vista o template 
	def get(self, request):	
		
		if request.method == "GET":
            
			# Accedo a la base de datos, específicamente a la tabla 'alertas' 
			ref = db.reference('Suel') 
			#print(ref.get())
			task=request.POST.get('task')
			#print(task)
			data = [1, 'foo']
			# Llamo los datos que se encuentran en la tabla 'alertas' 
			datos = ref.get()
			return render(request, self.template_name, { "data2": datos})
	

	
	#def home(request):
	#	data={}
		
	#	if request.method == "GET":
	#		print("hola")
	#		# auto random value if sendor is not connected , you can remove this line
	#		sensor_data=[]
	#		name = ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
	#		sensor_data.append(str(name))
	#		data['result']=sensor_data
	#	else:
	#		data['result']='Not Ajax'
	#	return JsonResponse(data)

	
