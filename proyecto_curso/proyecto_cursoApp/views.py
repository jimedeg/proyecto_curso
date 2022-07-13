from django.shortcuts import render,redirect
from django.http import HttpResponse

from proyecto_cursoApp.models import Curso, Evento
from .forms import *
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def inicio (request):
    
    curso = Curso.objects.all()[:3]
    evento = Evento.objects.all()[:3]
    
    return render(request,"proyecto_cursoApp/index.html",{'curso': curso , 'evento': evento})

def login_request(request):
    
    if request.method == "POST":
        
        form= AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
        else:
            return redirect("login")
    
    form = AuthenticationForm()
            
    return render(request,"proyecto_cursoApp/login.html",{"form": form})

def register_request(request):
    
    if request.method == "POST":
        
        form = UserCreationForm(request.POST)
        # form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            username= form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            form.save()
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
            
        
        return render(request,"proyecto_cursoApp/register.html",{"form": form})
    
    form = UserCreationForm()
    # form = UserRegisterForm()
    
    return render(request,"proyecto_cursoApp/register.html",{"form": form})

def logout_request(request):
    logout(request)
    return redirect("inicio")


def curso (request):
    
    if request.method == "POST":

        buscar = request.POST["buscar"]

        if buscar != "":
            curso = Curso.objects.filter( Q(nombre__icontains=buscar)).values()

            return render(request,"proyecto_cursoApp/curso.html",{"curso":curso, "buscar":True, "busqueda":buscar})

    curso = Curso.objects.all()

    return render(request,"proyecto_cursoApp/curso.html",{"curso":curso, "buscar":False})

@staff_member_required
def crear_curso (request):
    #post
    if request.method == "POST":
        
        formulario = nuevo_curso(request.POST)
        
        if formulario.is_valid():
            
            info_curso = formulario.cleaned_data
            
            curso = Curso(nombre = info_curso ["nombre"], info = info_curso ["informacion"], fecha = info_curso ["fecha"] )
            curso.save() #Guardar en la db
            
            return redirect("curso")
        else:
            return render(request,"proyecto_cursoApp/form_curso.html",{"form":formulario})
    else:
        
        formulario_vacio= nuevo_curso()
         
        return render(request,"proyecto_cursoApp/form_curso.html",{"form":formulario_vacio})

@staff_member_required
def editar_curso (request, curso_id):
 
    curso = Curso.objects.get(id=curso_id)
    
    if request.method == "POST":
        
        formulario = nuevo_curso(request.POST)
        
        if formulario.is_valid():
            
            info_curso = formulario.cleaned_data
            
            curso.nombre = info_curso ["nombre"]
            curso.info = info_curso ["informacion"]
            curso.fecha = info_curso ["fecha"]
            curso.save()
            
            return redirect("curso")
        
        else:
           return render(request,"proyecto_cursoApp/form_curso.html",{"form":formulario}) 
       
    else:
        formulario = nuevo_curso(initial={"nombre": curso.nombre, "informacion": curso.info, "fecha": curso.fecha})       
        
        return render(request,"proyecto_cursoApp/form_curso.html",{"form":formulario, "accion":"Editar Curso"})

@staff_member_required
def eliminar_curso (request, curso_id):
    
    curso = Curso.objects.get(id=curso_id)
    
    curso.delete()
    
    return redirect("curso")
            
def evento (request):
    
    evento = Evento.objects.all()
    
    return render(request,"proyecto_cursoApp/evento.html",{'evento': evento})

@staff_member_required
def crear_evento (request):
    #post
    if request.method == "POST":
        
        formulario = nuevo_evento(request.POST)
        
        if formulario.is_valid():
            
            info_evento = formulario.cleaned_data
            
            curso = Evento(nombre = info_evento ["nombre"], info = info_evento ["informacion"], fecha = info_evento ["fecha"] )
            
            return redirect("evento")
        else:
            return render(request,"proyecto_cursoApp/form_evento.html",{"form":formulario})
    else:
        
        formulario_vacio= nuevo_evento()
                 
        return render(request,"proyecto_cursoApp/form_evento.html",{"form":formulario_vacio})

def contacto (request):
    
    return render(request,"proyecto_cursoApp/contacto.html",{})

def busqueda (request):
         
    if request.method == "POST":
        
        nombre = request.POST["nombre"] 
             
        busquedas = Curso.objects.filter(nombre__icontains=nombre)
        
        return render(request,"proyecto_cursoApp/busqueda.html",{"busquedas": busquedas})
  
    else:
        
        busquedas=[]
        
        return render(request,"proyecto_cursoApp/busqueda.html",{"busquedas": busquedas})
       