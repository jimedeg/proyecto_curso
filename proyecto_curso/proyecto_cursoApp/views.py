from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio (request):
    
    return render(request,"proyecto_cursoApp/base.html",{})

def curso (request):
    
    return HttpResponse("Vista de los cursos")

def evento (request):
    
    return HttpResponse("Vista de eventos")

def contacto (request):
    
    return HttpResponse("Vista de contacto")