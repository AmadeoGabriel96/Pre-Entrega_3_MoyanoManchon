from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Curso(models.Model): 

    nombre = models.CharField(max_length=60)
    camada = models.IntegerField()

    def __str__(self):

        return f"{self.nombre} --- {self.camada}"

class Profesor(models.Model):

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    edad = models.IntegerField()
    email = models.EmailField()
    profesión = models.CharField(max_length=60)

    def __str__(self):

        return f"{self.nombre} --- {self.apellido}"

class Alumno(models.Model): 

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    edad = models.IntegerField()
    email = models.EmailField()   

    def __str__(self):

        return f"{self.nombre} --- {self.apellido}"

    
