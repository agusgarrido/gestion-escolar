from django import forms
from django.forms import ModelForm
from gestion.models import *

class DocenteForm(ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'ingreso_cargo': forms.DateInput(attrs={'type': 'date'})
        }

class AsignaturaForm(ModelForm):
    class Meta:
        model = Asignatura
        fields = '__all__'

class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'ingreso_institucion': forms.DateInput(attrs={'type': 'date'})
        }

