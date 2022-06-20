from django.shortcuts import render
from django.http import HttpResponse

from proyecto_cursoApp.models import Curso, Evento

# Create your views here.
def inicio (request):
    
    return render(request,"proyecto_cursoApp/index.html",{})

def curso (request):
    
    curso = Curso.objects.all()
    
    return render(request,"proyecto_cursoApp/curso.html",{'curso': curso})

def evento (request):
    
    evento = Evento.objects.all()
    
    return render(request,"proyecto_cursoApp/evento.html",{'evento': evento})

def contacto (request):
    
    return render(request,"proyecto_cursoApp/contacto.html",{})