from django.db import models
from django.contrib.auth.models import User

#modelo de Avatar 
class Avatar(models.Model):
    
    usuario = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatar/', blank=True)
    
# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    info = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    
class Evento(models.Model):
    nombre = models.CharField(max_length=50)
    info = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    mensaje = models.CharField(max_length=300)

class Comentario(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    mensaje = models.TextField(max_length=500, blank=True, null=True)
    actualizado = models.DateTimeField(auto_now=True)
    creado = models.DateTimeField(auto_now_add=True)   