from django.db import models
from django.contrib.auth.models import Group

class Curso(models.Model):
    curso = models.IntegerField()
    seccion = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.curso} "{self.seccion}"'
    
class Docente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    documento = models.IntegerField()
    ingreso_cargo = models.DateField()
    carga_horaria = models.IntegerField()

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
    
class Asignatura(models.Model):
    asignatura = models.CharField(max_length=200)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.asignatura} ({self.curso})'

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    documento = models.IntegerField()
    ingreso_institucion = models.DateField()
    curso = models.ForeignKey(Curso, related_name='alumnos', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'