from django.shortcuts import render, redirect
from .models import Alumno, Carrera, Materia
from .forms import alumnoForm, MateriaForm
#<< Create your views here.


def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'listaalumnos.html', {'alumnos': alumnos})

def lista_materias(request):
    materias = Materia.objects.select_related('carrera').all()
    return render(request, 'listamaterias.html', {'materias': materias})

def lista_carreras(request):
    carreras = Carrera.objects.all()
    return render(request, 'listacarreras.html', {'carreras': carreras})

def crear_materia(request):
    if request.method == 'POST':
        formulario = MateriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_materias')
    else:
        formulario = MateriaForm()

    return render(
        request,
        'crear_materia.html',
        {'formulario': formulario}
    )

def detalle_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    return render(request, 'detalle_alumno.html', {'alumno': alumno})

def crear_alumno(request):
    if request.method == 'POST':
        formulario = alumnoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_alumnos')
    else:
        formulario = alumnoForm()


    return render(
        request,
        'crear_alumno.html',
        {'formulario': formulario}
    )

def editar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    if request.method == 'POST':
        formulario = alumnoForm(request.POST, instance=alumno)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_alumnos')
    else:
        formulario = alumnoForm(instance=alumno)

    return render(
        request,
        'editar_alumno.html',
        {'formulario': formulario}
    )

def eliminar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    if request.method == 'POST':
        alumno.delete()
        return redirect('lista_alumnos')
    return render(
        request,
        'eliminar_alumno.html',
        {'alumno': alumno}
    )

        