from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio (request):
    
    return render(request,"proyecto_cursoApp/index.html",{})

def curso (request):
    
    return render(request,"proyecto_cursoApp/curso.html",{})

def evento (request):
    
    return render(request,"proyecto_cursoApp/evento.html",{})

def contacto (request):
    
    return render(request,"proyecto_cursoApp/contacto.html",{})