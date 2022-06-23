from django import forms

class nuevo_curso(forms.Form):
    
    nombre = forms.CharField(max_length= 30)
    informacion = forms.CharField(max_length=100)
    fecha = forms.DateField()