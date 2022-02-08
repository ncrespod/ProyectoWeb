# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    Empid= models.IntegerField()
    name= models.CharField(max_length=25)
    address= models.CharField(max_length=100)
    salary= models.IntegerField()
    Department= models.CharField(max_length=25)
