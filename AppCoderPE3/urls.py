from django.urls import path
from AppCoderPE3.views import *

urlpatterns = [
    path("", inicio),
    path("cursos/", curso, name="Cursos"), 
    path("profesores/", profesores, name="Profesores"), 
    path("alumnos/", alumnos, name="Alumnos"), 
    path("cursoFormulario/", cursoFormulario),
    path("buscarCamada/", buscarCamada),
    path("buscar/", buscar),
    path("guardar_curso/", guardar_curso, name="guardar_curso"),
    path("guardar_profesor/", guardar_profesor, name="guardar_profesor"),
    path("guardar_alumno/", guardar_alumno, name="guardar_alumno"),
    path("buscar_curso/", buscar_curso, name="buscar_curso"),
    path("buscar_profesor/", buscar_profesor, name="buscar_profesor"),
    path("buscar_alumno/", buscar_alumno, name="buscar_alumno"),
]