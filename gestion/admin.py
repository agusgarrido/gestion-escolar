from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Docente, Alumno, Asignatura, Curso

class DocenteAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'fecha_nacimiento', 'documento', 'ingreso_cargo']

class AlumnoAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'fecha_nacimiento', 'documento', 'ingreso_institucion', 'curso_id']

class AsignaturaAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['asignatura', 'curso_id', 'docente_id']


admin.site.register(Docente, DocenteAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Asignatura, AsignaturaAdmin)
admin.site.register(Curso)
