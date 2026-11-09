from django.contrib import admin
from .models import Alumno, Carrera, Materia

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Carrera)
admin.site.register(Materia)