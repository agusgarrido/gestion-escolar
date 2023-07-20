from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from gestion.models import *
from gestion.forms import *
from gestion.filters import *

# VENTANAS DE GESTIÓN

@login_required
def gestion(request):
    return render(request, 'gestion.html')

# DOCENTES

@login_required
def gestion_docentes(request):
    docentes = Docente.objects.all()
    return render(request, 'gestion_docentes.html', {'docentes': docentes})

@login_required
def agregarDocente(request):
    if request.method == 'POST':
        docenteForm = DocenteForm(request.POST)
        if docenteForm.is_valid():
            docenteForm.save()
            return redirect('docentes')
    else:
        docenteForm = DocenteForm()
    return render (request, 'agregar_docente.html', {'docenteForm': docenteForm})

@login_required
def editarDocente(request, id):
    docente = get_object_or_404(Docente, pk=id)
    if request.method == 'POST':
        docenteForm = DocenteForm(request.POST, instance = docente)
        if docenteForm.is_valid():
            docenteForm.save()
            return redirect('docentes')
    else:
        docenteForm = DocenteForm(instance = docente)
    return render(request, 'editar_docente.html', {'docenteForm': docenteForm})

@login_required
def eliminarDocente(request, id):
    docente = get_object_or_404(Docente, pk=id)
    if docente:
        docente.delete()
        return redirect('docentes')

# ASIGNATURAS

@login_required
def gestion_asignaturas(request):
    asignaturas = AsignaturaFilter(request.GET, queryset=Asignatura.objects.all())
    return render(request, 'gestion_asignaturas.html', {'asignaturas': asignaturas})

@login_required
def agregarAsignatura(request):
    if request.method == 'POST':
        asignaturaForm = AsignaturaForm(request.POST)
        if asignaturaForm.is_valid():
            asignaturaForm.save()
            return redirect('asignaturas')
    else:
        asignaturaForm = AsignaturaForm()
    return render (request, 'agregar_asignatura.html', {'asignaturaForm': asignaturaForm})

@login_required
def editarAsignatura(request, id):
    asignatura = get_object_or_404(Asignatura, pk=id)
    if request.method == 'POST':
        asignaturaForm = AsignaturaForm(request.POST, instance = asignatura)
        if asignaturaForm.is_valid():
            asignaturaForm.save()
            return redirect('asignaturas')
    else:
        asignaturaForm = AsignaturaForm(instance = asignatura)
    return render(request, 'editar_asignatura.html', {'asignaturaForm': asignaturaForm})

@login_required
def eliminarAsignatura(request, id):
    asignatura = get_object_or_404(Asignatura, pk=id)
    if asignatura:
        asignatura.delete()
        return redirect('asignaturas')
    
# ALUMNOS

@login_required
def gestion_alumnos(request):
    alumnos = AlumnoFilter(request.GET, queryset=Alumno.objects.all())
    return render(request, 'gestion_alumnos.html', {'alumnos': alumnos})

@login_required
def agregarAlumno(request):
    if request.method == 'POST':
        alumnoForm = AlumnoForm(request.POST)
        if alumnoForm.is_valid():
            alumnoForm.save()
            return redirect('alumnos')
    else:
        alumnoForm = AlumnoForm()
    return render (request, 'agregar_alumno.html', {'alumnoForm': alumnoForm})

@login_required
def editarAlumno(request, id):
    alumno = get_object_or_404(Alumno, pk=id)
    if request.method == 'POST':
        alumnoForm = AlumnoForm(request.POST, instance = alumno)
        if alumnoForm.is_valid():
            alumnoForm.save()
            return redirect('alumnos')
    else:
        alumnoForm = AlumnoForm(instance = alumno)
    return render(request, 'editar_alumno.html', {'alumnoForm': alumnoForm})

@login_required
def eliminarAlumno(request, id):
    alumno = get_object_or_404(Alumno, pk=id)
    if alumno:
        alumno.delete()
        return redirect('alumnos')