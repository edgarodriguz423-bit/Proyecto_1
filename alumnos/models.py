from django.db import models

# Create your models here.

class Alumno(models.Model):
    carrera = models.ForeignKey('Carrera', on_delete=models.CASCADE, verbose_name="Carrera")
    matricula = models.CharField(verbose_name="Matricula", max_length=10, unique=True)
    nombre = models.CharField(verbose_name="Nombre alumno", max_length=50)
    apellido_paterno = models.CharField(verbose_name="Apellido paterno", max_length=100)
    apellido_materno = models.CharField(verbose_name="Apellido materno", max_length=100)
    edad = models.IntegerField(verbose_name="Edad")
    fecha_registro = models.DateTimeField(verbose_name="Fecha de registro", auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"


class Carrera(models.Model):
    codigo = models.CharField(verbose_name="Código de la carrera", max_length=10, unique=True)
    nombre = models.CharField(verbose_name="Nombre de la carrera", max_length=100)
    duracion = models.IntegerField(verbose_name="Duración en cuatrimestres")
    fecha_registro = models.DateTimeField(verbose_name="Fecha de registro", auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.duracion} cuatrimestres) - Registrada: {self.fecha_registro}"


class Materia(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, verbose_name="Carrera")
    nombre = models.CharField(verbose_name="Nombre de la materia", max_length=100)

    def __str__(self):
        return self.nombre