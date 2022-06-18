from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio (request):
    
    return HttpResponse("vista de inicio")

def curso (request):
    
    return HttpResponse("Vista de los cursos")

def evento (request):
    
    return HttpResponse("Vista de eventos")