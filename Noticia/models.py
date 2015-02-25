from django.db import models
# Create your models here.

class Noticia(models.Model):
    titulo=models.TextField()
    imagen=models.FileField(upload_to='static/Noticia')
    descripcion=models.TextField()
    noticia=models.TextField()
    estado=models.BooleanField(default=True)

    def __unicode__(self):
        return "%s %s %s"%(self.titulo,self.descripcion,self.estado)
