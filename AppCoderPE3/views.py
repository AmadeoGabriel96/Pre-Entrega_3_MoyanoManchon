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

def cursoFormulario(request):

    formulario1 = CursoFormulario(request.POST)

    if request.method == "POST":

        formulario1 = CursoFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            profesor = Curso(nombre=info["profesor"], camada=info["camada"])

            profesor.save

            return render(request, "AppCoderPE3/inicio.html")

    else:

        formulario1 = CursoFormulario()        

    return render(request, "AppCoderPE3/cursoFormulario.html", {"form1":formulario1}) 

def buscarCamada(request):

    return render(request, "AppCoderPE3/buscarCamada.html") 

def buscar(request):

    if request.GET["camada"]:

        camada = request.GET["camada"]
        profesores = Curso.objects.filter(camada__iexact=camada)

        return render(request, "AppCoderPE3/buscar.html", {"profesores":profesores, "camada":camada})

    else:

        respuesta = "No enviaste datos"    

    return HttpResponse(respuesta)

def guardar_curso(request):

    if request.method == "POST":

        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():

            formulario.save()

            return redirect('Cursos')

    else:

        formulario = CursoFormulario()

        return render(request, "AppCoderPE3/cursoFormulario.html", {"form": formulario})

def buscar_curso(request):

    if 'nombre_curso' in request.GET:

        nombre_curso = request.GET['nombre_curso']

        cursos = Curso.objects.filter(nombre__icontains=nombre_curso)

        return render(request, "AppCoderPE3/buscar.html", {'cursos': cursos, 'tipo': 'curso'})

    else:

        return HttpResponse("No se proporcionaron datos de búsqueda para cursos.")

def guardar_profesor(request):

    if request.method == "POST":

        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():

            formulario.save()

            return redirect('Profesores')

    else:

        formulario = ProfesorFormulario()

        return render(request, "AppCoderPE3/profesorFormulario.html", {"form": formulario})

def buscar_profesor(request):

        if 'nombre_profesor' in request.GET:

        nombre_profesor = request.GET['nombre_profesor']

        profesores = Profesor.objects.filter(nombre__icontains=nombre_profesor)

        return render(request, "AppCoderPE3/buscar.html", {'profesores': profesores, 'tipo': 'profesor'})

    else:

        return HttpResponse("No se proporcionaron datos de búsqueda para profesores.")  

def guardar_alumno(request):

        if request.method == "POST":

        formulario = AlumnoFormulario(request.POST)

        if formulario.is_valid():

            formulario.save()

            return redirect('Alumnos')

    else:

        formulario = AlumnoFormulario()

        return render(request, "AppCoderPE3/alumnoFormulario.html", {"form": formulario})

def buscar_alumno(request):  

        if 'nombre_alumno' in request.GET:

        nombre_alumno = request.GET['nombre_alumno']

        alumnos = Alumno.objects.filter(nombre__icontains=nombre_alumno)

        return render(request, "AppCoderPE3/buscar.html", {'alumnos': alumnos, 'tipo': 'alumno'})

    else:

        return HttpResponse("No se proporcionaron datos de búsqueda para alumnos.") 






 