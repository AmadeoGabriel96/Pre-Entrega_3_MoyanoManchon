from django.db import models

# Create your models here.

class Curso(models.Model): 

    nombre = models.CharField(max_length=60)
    camada = models.IntegerField()

class Profesor(models.Model):

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    edad = models.IntegerField()
    email = models.EmailField()
    profesión = models.CharField(max_length=60)

class Alumno(models.Model): 

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    edad = models.IntegerField()
    email = models.EmailField()   