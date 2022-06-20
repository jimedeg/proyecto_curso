from django.contrib import admin

# Register your models here.
from proyecto_cursoApp.models import Curso, Evento

# Register your models here.
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'info', 'fecha')

admin.site.register(Curso, CursoAdmin)

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'info', 'fecha')

admin.site.register(Evento, EventoAdmin)

#user= admin - contraseña= 1234