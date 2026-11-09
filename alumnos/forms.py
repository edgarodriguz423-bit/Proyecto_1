from django import forms
from .models import Alumno, Materia

class alumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['carrera', 'matricula', 'nombre', 'apellido_paterno', 'apellido_materno','edad']


class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre', 'carrera']