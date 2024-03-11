from django.shortcuts import render
from django.http import HttpResponse
from AppCoderPE3.forms import CursoFormulario
from AppCoderPE3.models import Curso 

# Create your views here.

def inicio(request):

    return render(request,"AppCoderPE3/inicio.html")

def profesor(request):

    return render(request, "AppCoderPE3/profesores.html")

def profesores(request):

    return render(request,"AppCoderPE3/profesores.html")

def alumnos(request):

    return render(request,"AppCoderPE3/alumnos.html")

