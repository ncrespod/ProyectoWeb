from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View 
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from firebase_admin import credentials
from firebase_admin import db

class Reg(View):
	template_name = "tables-simple.html"

	def get(self, request):	
		
		if request.method == "GET":
			ref = db.reference('Suel') 
			datos = ref.get()
			return render(request, self.template_name, { "data2": datos})

	
