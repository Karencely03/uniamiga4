#Django
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Models
from .models import *


class PacienteForm(forms.ModelForm):
    class Meta:
        model = estudiantes
        fields = '__all__'
        exclude = ['user']


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = '__all__'
        exclude = ['user']


class UserCreationForm(UserCreationForm):
    Users = [
        ('M', 'Tutor'),
        ('P', 'Estudiante')
    ]
    tipo_usuario = forms.ChoiceField(required=True, choices=Users)

    
    # first_name = forms.CharField(max_length=45, required=True, label='Nombres')
    # last_name = forms.CharField(max_length=45, required=True, label='Apellidos')

    # class Meta:
    #     model = User
    #     fields = ['first_name', 'last_name', 'username', 'password']
    #     labels = {
    #         'first_name': 'Nombres',
    #         'last_name': 'Apellidos',
    #         'username': 'Email',
    #     }

class CursosForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields =['Nombre','Descripcion']

class IncripcionForm(forms.ModelForm):
    class Meta:
        model=Inscripcion
        fields=['Cursos']



class RegistradoForm(forms.ModelForm):
    class Meta:
        model=Archivo
        fields=['Nombre','Descripcion','Media','Curso']
