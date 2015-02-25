from django.db import models
from Estudiantes.models import Estudiantes

class Tipo_Tramite(models.Model):
    tipo_tramite=models.CharField(max_length=100)

    def __unicode__(self):
        return "%s"%(self.tipo_tramite)

class Turno(models.Model):
    estudiante=models.ForeignKey(Estudiantes,null=True)
    tipo_tramite=models.ForeignKey(Tipo_Tramite, null=True)
    fecha=models.DateTimeField()

    def __unicode__(self):
        return "%s %s %s %s"%(self.estudiante.id,self.estudiante.cedula,self.tipo_tramite.tipo_tramite,self.fecha)

