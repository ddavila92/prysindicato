from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin

class Estudiantes(models.Model):
    usuario=models.ForeignKey(User)
    cedula=models.CharField(max_length=13)
    cert_votacion=models.CharField(max_length=13)
    fecha_nacimiento=models.DateField()
    lugar_nacimiento=models.CharField(max_length=100)
    nacionalidad=models.CharField(max_length=100)
    telefono=models.CharField(max_length=15)
    tipo_sangre=models.CharField(max_length=5)
    direccion=models.CharField(max_length=100)
    nombre_colegio=models.TextField()
    anio_graduacion=models.CharField(max_length=5)
    sexo=models.CharField(max_length=20)

    def __unicode__(self):
        return "%s %s"%(self.usuario.first_name,self.usuario.last_name)