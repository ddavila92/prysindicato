from django.db import models
from Estudiantes.models import Estudiantes

class Periodo(models.Model):
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()

    def __unicode__(self):
        return "%s / %s "%(self.fecha_inicio, self.fecha_fin)

class Seccion(models.Model):
    seccion=models.CharField(max_length=50)
    dias=models.CharField(max_length=50)
    tiempo=models.CharField(max_length=50)

    def __unicode__(self):
        return "%s"%(self.seccion)

class Paralelo(models.Model):
    paralelo=models.CharField(max_length=10)
    cupo=models.IntegerField()

    def __unicode__(self):
        return "%s, %s"%(self.paralelo,self.cupo)

class Matricula(models.Model):
    estudiante=models.ForeignKey(Estudiantes, unique=True)
    periodo=models.ForeignKey(Periodo)
    seccion=models.ForeignKey(Seccion)
    paralelo=models.ForeignKey(Paralelo)
    estado=models.BooleanField()

    def __unicode__(self):
        return "%s, %s, %s, %s, %s, %s, %s"%(self.estudiante.usuario.first_name, self.estudiante.usuario.last_name, self.paralelo.paralelo, self.seccion.seccion, self.periodo.fecha_inicio,self.periodo.fecha_fin,self.estado)


