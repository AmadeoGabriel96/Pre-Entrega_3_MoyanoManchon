from django.urls import path
from AppCoderPE3.views import *

urlpatterns = [
    path("", inicio),
    path("cursos/", curso, name="Cursos"), 
    path("profesores/", profesores, name="Profesores"), 
    path("alumnos/", alumnos, name="Alumnos"), 
]
