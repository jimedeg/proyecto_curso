from distutils.log import info
from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    info = models.CharField(max_length=50)
    comision = models.IntegerField()
    
class Evento(models.Model):
    nombre = models.CharField(max_length=10)
    info = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    