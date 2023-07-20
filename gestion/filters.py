import django_filters
from .models import *

class AlumnoFilter(django_filters.FilterSet):
    class Meta:
        model = Alumno
        fields = '__all__'
        exclude = ['nombre', 'apellido', 'fecha_nacimiento', 'documento', 'ingreso_institucion']

class AsignaturaFilter(django_filters.FilterSet):
    class Meta:
        model = Asignatura
        fields = '__all__'
        exclude = ['asignatura', 'docente']