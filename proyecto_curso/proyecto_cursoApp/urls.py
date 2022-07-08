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
    path ('curso', curso, name= "curso"),
    path ('evento', evento, name= "evento"),
    path ('contacto', contacto, name= "contacto"),
    path ('crear_curso', crear_curso, name= "crear_curso"),
    path ('busqueda', busqueda, name= "busqueda"),
    path ('login', login_request, name= "login"),
    path ('register', register_request, name= "register"),
    ]
