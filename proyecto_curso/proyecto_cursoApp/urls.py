"""proyecto_curso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import *

urlpatterns = [
    path ('', inicio, name= "inicio" ),
     path ('login', login_request, name= "login"),
    path ('register', register_request, name= "register"),
    path ('logout', logout_request, name= "logout"),
    
    path ('curso', curso, name= "curso"),
    path ('crear_curso', crear_curso, name= "crear_curso"),
    path ('editar_curso/<curso_id>/', editar_curso, name= "editar_curso"),
    path ('eliminar_curso/<curso_id>/', eliminar_curso, name= "eliminar_curso"),
    
    path ('evento', evento, name= "evento"),
    path ('crear_evento', crear_evento, name= "crear_evento"),
    path ('editar_evento/<evento_id>/', editar_evento, name= "editar_evento"),
    path ('eliminar_evento/<evento_id>/', eliminar_evento, name= "eliminar_evento"),
    
    path ('contacto', contacto, name= "contacto"),
    
    path ('busqueda', busqueda, name= "busqueda"),
   
    
    ]
