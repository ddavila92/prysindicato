from django.db import models

# Create your models here.
from Profesor.models import Profesor


class Materia(models.Model):
    materia=models.CharField(max_length=100)

    def __unicode__(self):
        return "%s"%(self.materia)

class Profesor_Materia(models.Model):
    materia=models.ForeignKey(Materia)
    profesor=models.ForeignKey(Profesor)

    def __unicode__(self):
        return "%s %s "%(self.materia,self.profesor)