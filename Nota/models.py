from django.db import models

# Create your models here.
from Estudiantes.models import Estudiantes
from Materia.models import Materia


class Nota(models.Model):
    materia=models.ForeignKey(Materia)
    estudiante=models.ForeignKey(Estudiantes)
    deber=models.FloatField()
    actuacion=models.FloatField()
    leccion=models.FloatField()
    examen=models.FloatField()
    supletorio=models.FloatField()

    def __unicode__(self):
        return "%s %s %s %s %s %s "%(self.materia,self.estudiante,self.deber,self.actuacion,self.leccion,self.examen)