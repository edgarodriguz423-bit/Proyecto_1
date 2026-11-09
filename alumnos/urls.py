from django.urls import path
from . import views
urlpatterns = [
    path('lista_alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('materias/', views.lista_materias, name='lista_materias'),
    path('carreras/', views.lista_carreras, name='lista_carreras'),
    path('crear_materia/', views.crear_materia, name='crear_materia'),
    path('detalle_alumno/<int:id>/', views.detalle_alumno, name='detalle_alumno'),
    path('crear_alumno/', views.crear_alumno, name='crear_alumno'),
    path('editar_alumno/<int:id>/', views.editar_alumno, name='editar_alumno'),
    path('eliminar_alumno/<int:id>/', views.eliminar_alumno, name='eliminar_alumno'),
]