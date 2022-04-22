from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View 
from django.http import HttpResponse, JsonResponse
from datetime import datetime
import random
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Reg4(View):
	template_name = "tables-simple4.html"

	def get(self, request):	
		if request.method == "GET":
			ref = db.reference('Luz')
			datos = ref.get()
			return render(request, self.template_name, { "data4": datos})