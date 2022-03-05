from django.db import models
from django.utils import timezone
import firebase_admin
# Create your models here.
class alertasAP4(models.Model):
    Nombre = models.CharField(max_length=100)
    Dato = models.CharField(max_length=100)
    Descripcion = models.CharField(max_length=100)

    def publish(self):
        self.Nombre = timezone.now()
        self.save()