"""
URL configuration for gestionescolar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
from django.urls import path
from gestion.views import *
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', gestion),
    path('docentes/', gestion_docentes, name="docentes"),
    path('asignaturas/', gestion_asignaturas, name="asignaturas"),
    path('editar_docente/<int:id>/', editarDocente, name="editar_docente"),
    path('agregar_docente/', agregarDocente, name="agregar_docente"),
    path('eliminar_docente/<int:id>/', eliminarDocente, name='eliminar_docente'),
    path('editar_asignatura/<int:id>/', editarAsignatura, name="editar_asignatura"),
    path('agregar_asignatura/', agregarAsignatura, name="agregar_asignatura"),
    path('eliminar_asignatura/<int:id>/', eliminarAsignatura, name='eliminar_asignatura'),
    path('alumnos/', gestion_alumnos, name="alumnos"),
    path('editar_alumno/<int:id>/', editarAlumno, name="editar_alumno"),
    path('agregar_alumno/', agregarAlumno, name="agregar_alumno"),
    path('eliminar_alumno/<int:id>/', eliminarAlumno, name='eliminar_alumno'),
    path ('logout/', logout_then_login, name='logout')
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()