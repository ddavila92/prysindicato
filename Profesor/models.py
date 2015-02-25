from django.contrib.auth.models import User
from django.db import models
from Matricula.models import Paralelo


class Profesor(models.Model):
    usuario=models.ForeignKey(User)
    paralelo=models.ForeignKey(Paralelo)
    nombre=models.CharField(max_length=60)
    apellido=models.CharField(max_length=60)
    cedula=models.CharField(max_length=15)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=15)
    correo=models.CharField(max_length=100)
    titulo=models.CharField(max_length=100)

    def __unicode__(self):
        return "%s %s"%(self.nombre,self.apellido)