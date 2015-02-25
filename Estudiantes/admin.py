from django.contrib import admin
from django.contrib.admin.sites import site
from Estudiantes.models import Estudiantes

class EstudiantesAdmin(admin.ModelAdmin):
    list_display = ("usuario","cedula","cert_votacion","sexo")
    search_fields = ["cedula"]
    list_filter = ["cedula"]

site.register(Estudiantes,EstudiantesAdmin)
