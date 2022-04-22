from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Alertas(View):

	template_name = "tables-data.html"
	cred = credentials.Certificate('./cacaotech-50682-firebase-adminsdk-3gp64-5222c7f14f.json')
	firebase_admin.initialize_app(cred, {
	    'databaseURL': 'https://cacaotech-50682-default-rtdb.firebaseio.com'
	})
	ref = db.reference('Alertas2') 
	datos = ref.get()

	def get(self, request):	
		if request.method == "GET":
			ref = db.reference('Alertas2') 
			datos = ref.get()
			return render(request, self.template_name, { "data": datos})

	