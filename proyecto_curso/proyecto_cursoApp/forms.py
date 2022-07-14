from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class nuevo_curso(forms.Form):
    
    nombre = forms.CharField(max_length= 30)
    informacion = forms.CharField(max_length=100)
    fecha = forms.DateField()
    
class nuevo_evento(forms.Form):
    nombre = forms.CharField(max_length= 30)
    informacion = forms.CharField(max_length=100)
    fecha = forms.DateField()    
    
class UserRegisterForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña",  widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields= ['username', 'first_name', 'last_name', 'email', 'password1', 'password2'] 
        
        # help_texts= {k:"" for k in fields}
        
class UserEditForm(UserCreationForm):
    
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    
    email= forms.EmailField(label="Email")
    password1: forms.CharField(label="Contraseña",  widget=forms.PasswordInput, required=False)
    password2: forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)
    
    
    class Meta:
        model = User
        fields= ['first_name', 'last_name', 'email', 'password1', 'password2']
         