from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View 


# Importo Firebase Admin SDK 
import firebase_admin

# Definimos las credenciales que nos permitirán usar Firebase Admin SDK 
from firebase_admin import credentials

# Importo el Servicio Firebase Realtime Database 
from firebase_admin import db


class Alertas(View):

	# Especifico la plantilla o template que usaré 
	template_name = "tables-data.html"

	# Llamo al archivo JSON que contiene mi clave privada 
	cred = credentials.Certificate('./cacaotech-50682-firebase-adminsdk-3gp64-5222c7f14f.json')

	# Iniciamos los servicios de Firebase con las credenciales y el nombre de mi proyecto en Firebase 
	firebase_admin.initialize_app(cred, {
	    'databaseURL': 'https://cacaotech-50682-default-rtdb.firebaseio.com'
	})

	# Accedo a la base de datos, específicamente a la tabla 'alertas' 
	ref = db.reference('Alertas2') 
	#print(ref.get())

	# Llamo los datos que se encuentran en la tabla 'alertas' 
	datos = ref.get()

	# Envio los datos de la tabla 'alertas' a la vista o template 
	def get(self, request):	
		if request.method == "GET":

			# Accedo a la base de datos, específicamente a la tabla 'alertas' 
			ref = db.reference('Alertas2') 
			#print(ref.get())

			# Llamo los datos que se encuentran en la tabla 'alertas' 
			datos = ref.get()
			return render(request, self.template_name, { "data": datos})

	