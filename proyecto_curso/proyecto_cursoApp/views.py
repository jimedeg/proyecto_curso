from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio (request):
    
    return render(request,"proyecto_cursoApp/index.html",{})

def curso (request):
    
    return render(request,"proyecto_cursoApp/curso.html",{})

def evento (request):
    
    return HttpResponse("Vista de eventos")

def contacto (request):
    
    return HttpResponse("Vista de contacto")