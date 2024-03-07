from django import forms 

class CursoFormulario(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()

class ProfesorFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms,CharField()
    profesión = forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()

class AlumnoFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms,CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()        
