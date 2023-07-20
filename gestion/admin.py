from django.contrib import admin

from .models import Docente, Alumno, Asignatura, Curso
admin.site.register(Docente)
admin.site.register(Alumno)
admin.site.register(Asignatura)
admin.site.register(Curso)
